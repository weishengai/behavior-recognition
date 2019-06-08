# coding=utf8


class actionPredictor(object):

    def __init__(self):
        pass

    @staticmethod
    def move_status(joints):

        # body center (neck + rHip + lHip) / 3
        init_x = float(joints[0][1][0] + joints[0][8][0] + joints[0][11][0]) / 3
        init_y = float(joints[0][1][1] + joints[0][8][1] + joints[0][11][1]) / 3
        end_x = float(joints[-1][1][0] + joints[-1][8][0] + joints[-1][11][0]) / 3
        end_y = float(joints[-1][1][1] + joints[-1][8][1] + joints[-1][11][1]) / 3

        # upper body length: (rHip + lHip)/2 - neck
        init_h1 = float(joints[0][8][1] + joints[0][11][1]) / 2 - joints[0][1][1]
        end_h1 = float(joints[-1][8][1] + joints[-1][11][1]) / 2 - joints[-1][1][1]
        try:
            # ratio of upper body ending / beginning
            h1 = end_h1 / init_h1
        except:
            h1 = 0.0

        # lower part body length: ( (RKnee + LKnee) - (RHip + LHip) ) / 2
        init_h2 = (float(joints[0][9][1] + joints[0][12][1]) - float(joints[0][8][1] + joints[0][11][1])) / 2
        end_h2 = (float(joints[-1][9][1] + joints[-1][12][1]) - float(joints[-1][8][1] + joints[-1][11][1])) / 2

        try:
            # beginning frame to ending frame lower part body length ratio
            h2 = end_h2 / init_h2
        except:
            h2 = 0.0

        # changes between 15 frames
        xc = end_x - init_x
        yc = end_y - init_y
        if abs(xc) < 30. and abs(yc) < 20.:
            # Neck
            ty_1 = float(joints[-1][1][1])
            # Hip
            ty_8 = float(joints[-1][8][1] + joints[-1][11][1]) / 2
            # Knee
            ty_9 = float(joints[-1][9][1] + joints[-1][12][1]) / 2
            try:
                # Upper body to lower body heigh ratio
                t = float(ty_8 - ty_1) / (ty_9 - ty_8)
            except:
                t = 0.0

            # no movement between frames
            if h1 < 1.16 and h1 > 0.84 and h2 < 1.16 and h2 > 0.84:

                if t < 1.73:
                    return 1
                else:
                    return 2
            # moving
            else:
                # ?
                if t < 1.7:
                    # walk close
                    if h1 >= 1.08:
                        return 4

                    elif h1 < 0.92:
                        return 5
                    else:
                        return 0
                else:
                    return 0
        # check Y change, stand up
        elif abs(xc) < 30. and abs(yc) >= 20.:
            init_y1 = float(joints[0][1][1])
            init_y8 = float(joints[0][8][1] + joints[0][11][1]) / 2
            init_y9 = float(joints[0][9][1] + joints[0][12][1]) / 2

            end_y1 = float(joints[-1][1][1])
            end_y8 = float(joints[-1][8][1] + joints[-1][11][1]) / 2
            end_y9 = float(joints[-1][9][1] + joints[-1][12][1]) / 2
            # upper body to lower boy ratio
            try:
                init_yc = float(init_y8 - init_y1) / (init_y9 - init_y8)
            except:
                init_yc = 0.0
            try:
                end_yc = float(end_y8 - end_y1) / (end_y9 - end_y8)
            except:
                end_yc = 0.0

            th_yc = 0.07
            th_yc_down = 0.15

            if yc >= 25 and end_yc - init_yc >= th_yc_down:
                return 8
            elif yc >= 20 and abs(end_yc - init_yc) >= th_yc and abs(end_yc - init_yc) < th_yc_down:
                return 6
            elif yc < -20 and abs(end_yc - init_yc) >= th_yc_down:
                return 7
            else:
                return 0
        elif abs(xc) > 30. and abs(yc) < 30.:
            return 3
        else:
            return 0
