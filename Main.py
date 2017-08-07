# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project

# Analyze Results from PIL built-in quantizer


# PIL for manipulating images
import PIL
from PIL import Image
# time for stopwatch capability
import time
import math



# Read Image #
def readImage(choice):
   # print('in readImage')

    # Images
    pic1 = "Bikes.JPG"
    pic2 = "Birds.jpg"
    pic3 = "Boats.JPG"
    pic4 = "Girl.JPG"
    pic5 = "Hats.JPG"
    pic6 = "Lena.JPG"
    pic7 = "Mandrill.JPG"
    pic8 = "Peppers.JPG"



##### User selects image to use
    if (choice == 1):
        picture = pic1
    elif (choice == 2):
        picture = pic2
    elif (choice == 3):
        picture = pic3
    elif (choice == 4):
        picture = pic4
    elif (choice == 5):
        picture = pic5
    elif (choice == 6):
        picture = pic6
    elif (choice == 7):
        picture = pic7
    elif (choice == 8):
        picture = pic8
    else:
        picture = pic1

    im = Image.open(picture)
    # im.show()


    return(im)
# end of readImage #



# gather all information as in SSE, MSE, MAE from images #
def Measurements(im, pilQ):
    print("In Measurements")
    # all the pixels in order to compare
    OrigPixels = im.load()
    qPixels = pilQ.load()
    width = int(pilQ.size[0])
    length = int(pilQ.size[1])
    s = 0
    m = 0

    # calculate SSE by adding up all distances (each point to its cluster centroid)
    for y in range(0, length):
        for x in range(0, width):
            # find distance between the two
            a = OrigPixels[x, y]
            b = qPixels[x, y]

            # find distance between the two points
            red = a[0] - b[0]
            R = red * red
            green = a[1] - b[1]
            G = green * green
            blue = a[2] - b[2]
            B = blue * blue
            dist2 = R + G + B  # NO SQRT

            # squared distances added
            s += dist2
            # add the absolute distance of each color
            m += (math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1]) + math.fabs(a[2] - b[2]))

    # mean squared error
    mse = s / (length * width)
    # mean absolute error
    mae = m / (length * width)

    # Tuple to return
    output = (s, mse, mae)

    print("SSE: " + str(s))
    print("MSE: " + str(mse))
    print("MAE: " + str(mae))


    return(output)
# end of Measurements #



# output files with info #
def out():

    # master output with all results
    master = open("PIL_Master.txt", "w")
    # all output files per Results file for copying over into Excel
    fnSSE = "PIL_Metrics_SSE.txt"
    outSSE = open(fnSSE, "w")
    fnMSE = "PIL_Metrics_MSE.txt"
    outMSE = open(fnMSE, "w")
    fnMAE = "PIL_Metrics_MAE.txt"
    outMAE = open(fnMAE, "w")
    fnTime = "PIL_Metrics_Time.txt"
    outTime = open(fnTime, "w")

    for x in range(1, 9):
        # go through all eight images
        im = readImage(x)


        # go through all k values for each image
        k = 8
        while (k < 300 ):
            # gather time it takes to quantize
            start = time.time()
            q = im.quantize(k)
            end = time.time()
            TIME = end - start

            # read in JPG version for comparisons
            fn = "PILquantizer_" + str(x) + "_" + str(k) + ".JPG"
            pilQ = Image.open(fn)

            metrics = Measurements(im, pilQ)

            SSE = metrics[0]
            MSE = metrics[1]
            MAE = metrics[2]


            # OUTPUT TO FILES
            master.write(str(x) + ", " + str(k) + ", " + str(SSE) + ", " + str(MSE) + ", " + str(MAE) + ", " + str(TIME) + "\n")
            outSSE.write(str(SSE) + "\n")
            outMSE.write(str(MSE) + "\n")
            outMAE.write(str(MAE) + "\n")
            outTime.write(str(TIME) + "\n")

            # increment k / number of clusters
            k = (k * 2) # 8, 16, 32, 64, 128, 256


    # close files for analysis after
    outSSE.close()
    outMSE.close()
    outMAE.close()
    outTime.close()
    master.close()

    return(1)
# end of out #



# Call Everything from Main #
def main():
    print("PIL built-in quantizer metrics")

    complete = out()

    if (complete == 1):
        print("Check output files")
# end of main #



# Call Main #
if __name__ == '__main__':
    main()
    # end of program #