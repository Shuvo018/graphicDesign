from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def translate_rectangle(p, t):
        fig, ax = plt.subplots()

        original_rectangle  = Rectangle((p[0][0],p[0][1]), p[1][0], p[1][1], fill=None, edgecolor="r")
        print("ccc")
        ax.add_patch(original_rectangle)
        p[0][0] += t[0]
        p[0][1] -= t[1]
        translated_rectangle  = Rectangle((p[0][0],p[0][1]), p[1][0], p[1][1], fill=None, edgecolor="b")
        ax.add_patch(translated_rectangle)
        ax.set_xlim([0, 20])
        ax.set_ylim([0, 20])
        plt.show()

        
if __name__ == "__main__":
        p = [[5,8], [8, 6]] # x, y and width, hight
        t = [2,1]
        translate_rectangle(p,t)
