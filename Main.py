# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project

# Analyze Results from PIL built-in quantizer

# output files with info #
def out():
    x = 0

    # all output files per Results file for copying over into Excel
    fnSSE = "Metrics_SSE_" + str(x) + ".txt"
    outSSE = open(fnSSE, "w")
    fnMSE = "Metrics_MSE_" + str(x) + ".txt"
    outMSE = open(fnMSE, "w")
    fnMAE = "Metrics_MAE_" + str(x) + ".txt"
    outMAE = open(fnMAE, "w")
    fnTime = "Metrics_Time_" + str(x) + ".txt"
    outTime = open(fnTime, "w")


    k = 8
    while (k < 300 ):


        # increment k / number of clusters
        k = (k * 2) # 8, 16, 32, 64, 128, 256


# end of out #



# Call Everything from Main #
def main():
    print("PIL built-in quantizer metrics")
# end of main #



# Call Main #
if __name__ == '__main__':
    main()
    # end of program #