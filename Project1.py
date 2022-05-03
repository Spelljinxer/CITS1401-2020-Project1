#Author Spelljinxer

def main(csvfile, year, type):
    fname = csvfile
    infile = open(fname, 'r')
    with infile as a:
        rainfall = [line.strip().split(',') for line in a] #split the list of lists with ","
    for x in rainfall:
        if x[-1] == '':
           x[-1] = '0.0'
    year_one = []
    year_two = []
    month1 = []
    month1b = []
    month2 = []
    month2b = []
    month3 = []
    month3b = []
    month4 = []
    month4b = []
    month5 = []
    month5b = []
    month6 = []
    month6b = []
    month7 = []
    month7b = []
    month8 = []
    month8b = []
    month9 = []
    month9b = []
    month10 = []
    month10b = []
    month11 = []
    month11b = []
    month12 = []
    month12b= []
    if type == "stats":   
        for x in rainfall[1:]:
            if x[1] == str(year):
              if x[2] == '1':
                 month1.append(x[-1])
              elif x[2] == '2':
                 month2.append(x[-1])
              elif x[2] == '3':
                 month3.append(x[-1])
              elif x[2] == '4':
                 month4.append(x[-1])
              elif x[2] == '5':
                 month5.append(x[-1])
              elif x[2] == '6':
                 month6.append(x[-1])
              elif x[2] == '7':
                 month7.append(x[-1])
              elif x[2] == '8':
                 month8.append(x[-1])
              elif x[2] == '9':
                 month9.append(x[-1])
              elif x[2] == '10':
                 month10.append(x[-1])
              elif x[2] == '11':
                 month11.append(x[-1])
              elif x[2] == '12':
                 month12.append(x[-1])
        grouped_Months = ([month1] + [month2] + [month3] + [month4] + [month5] + [month6] +
                    [month7] + [month8] + [month9] + [month10] + [month11] + [month12] )
            
        rainfall_List = [[float(item) for item in x] for x in grouped_Months] #convert to float
        mx1 = maximum_rainfall(rainfall_List)
        mn1 = minimum_rainfall(rainfall_List)
        avg1 = average_rainfall(rainfall_List)
        std1 = standard_deviation(rainfall_List)
        return (mx1, mn1, avg1, std1)
        
    elif type == "corr":
        for x in rainfall[1:]:
            if x[1] == str(year[1]):
              if x[2] == '1':
                 month1b.append(x[-1])
              elif x[2] == '2':
                 month2b.append(x[-1])
              elif x[2] == '3':
                 month3b.append(x[-1])
              elif x[2] == '4':
                 month4b.append(x[-1])
              elif x[2] == '5':
                 month5b.append(x[-1])
              elif x[2] == '6':
                 month6b.append(x[-1])
              elif x[2] == '7':
                 month7b.append(x[-1])
              elif x[2] == '8':
                 month8b.append(x[-1])
              elif x[2] == '9':
                 month9b.append(x[-1])
              elif x[2] == '10':
                 month10b.append(x[-1])
              elif x[2] == '11':
                 month11b.append(x[-1])
              elif x[2] == '12':
                 month12b.append(x[-1])
            elif x[1] == str(year[0]):
                if x[2] == '1':
                 month1.append(x[-1])
                elif x[2] == '2':
                    month2.append(x[-1])
                elif x[2] == '3':
                    month3.append(x[-1])
                elif x[2] == '4':
                    month4.append(x[-1])
                elif x[2] == '5':
                    month5.append(x[-1])
                elif x[2] == '6':
                    month6.append(x[-1])
                elif x[2] == '7':
                    month7.append(x[-1])
                elif x[2] == '8':
                    month8.append(x[-1])
                elif x[2] == '9':
                    month9.append(x[-1])
                elif x[2] == '10':
                    month10.append(x[-1])
                elif x[2] == '11':
                    month11.append(x[-1])
                elif x[2] == '12':
                    month12.append(x[-1])
                 
        year_one = ([month1] + [month2] + [month3] + [month4] + [month5] + [month6] +
                   [month7] + [month8] + [month9] + [month10] + [month11] + [month12] )
        year_two = ([month1b] + [month2b] + [month3b] + [month4b] + [month5b] + [month6b] +
                   [month7b] + [month8b] + [month9b] + [month10b] + [month11b] + [month12b] )
        for x in year_one:
            if x[-1] == '':
               x = '0.0'
        for x in year_two:
            if x[-1] == '':
               x[-1] = '0.0'
        y1 = [[float(item) for item in x] for x in year_one]   #lines 138-139 convert them to floats
        y2 = [[float(item) for item in x] for x in year_two]
        
        mx1 = maximum_rainfall(y1)
        mn1 = minimum_rainfall(y1)
        average1 = average_rainfall(y1)
        std1 = standard_deviation(y1)
        mx2 = maximum_rainfall(y2)
        mn2 = maximum_rainfall(y2)
        average2 = average_rainfall(y2)
        std2 = standard_deviation(y2) 
        
        #calculates average
        product_avg = [average1[i] * average2[i] for i in range(len(average1))]
        y1_sq = [average1[i] ** 2 for i in range(len(average1))]
        y2_sq = [average2[i] ** 2 for i in range(len(average2))]
        y1_SquareSum = sum(y1_sq)
        y1_Sum = sum(average1)
        y2_SquareSum = sum(y1_sq)
        y2_Sum = sum(average2)
        sm_size = len(average1)
        product_sum = sum(product_avg) #sum of all the product lists
        formula_one = (sm_size * product_sum) - (y1_Sum * y2_Sum) #lines 122-125 create formulas
        formula_two = (((sm_size * y1_SquareSum) - (y1_Sum**2)) ** (1/2))
        formula_three = (((sm_size * y2_SquareSum) - (y2_Sum**2)) ** (1/2))
        try:
            cm_formula = formula_one/(formula_two * formula_three)    #combine all formulas into one
        except:
            cm_formula = 0.0     
        avg_corr = round(cm_formula, 4)      #accounting for potential 0.0 values in the data
        
        #calculates standard deviation
        product_std = [std1[i] * std2[i] for i in range(len(std1))]
        y1_sq = [std1[i] ** 2 for i in range(len(std1))]
        y2_sq= [std2[i] ** 2 for i in range(len(std2))]
        y1_SquareSum = sum(y1_sq)
        y1_Sum = sum(average1)
        y2_SquareSum = sum(y1_sq)
        y2_Sum = sum(average2)
        sm_size = len(average1)
        product_sum = sum(product_std)
        formula_one = (sm_size * product_sum) - (y1_Sum * y2_Sum)       #same thing for lines 122-129
        formula_two = (((sm_size * y1_SquareSum) - (y1_Sum**2)) ** (1/2)) 
        formula_three = (((sm_size * y2_SquareSum) - (y2_Sum**2)) ** (1/2))
        try:
            cm_formulaTwo = formula_one/(formula_two * formula_three)
        except:
            cm_formulaTwo = 0.0
        std_corr = round(cm_formulaTwo, 4)
        
        #calculates maximum
        product_max = [mx1[i] * mx2[i] for i in range(len(mx1))]
        y1_sq = [mx1[i] ** 2 for i in range(len(mx1))]
        y2_sq = [mx2[i] ** 2 for i in range(len(mx2))]
        y1_SquareSum = sum(y1_sq)
        y1_Sum = sum(average1)
        y2_SquareSum = sum(y1_sq)
        y2_Sum = sum(average2)
        sm_size = len(average1)
        product_sum = sum(product_max)
        formula_one = (sm_size * product_sum) - (y1_Sum * y2_Sum)
        formula_two = (((sm_size * y1_SquareSum) - (y1_Sum**2)) ** (1/2))
        formula_three = (((sm_size * y2_SquareSum) - (y2_Sum**2)) ** (1/2))
        try:
            cm_formulaThree = formula_one/(formula_two * formula_three)
        except:
            cm_formulaThree = 0.0
        max_corr = cm_formulaThree
        
        #calculates minimum
        product_min = [mn1[i] * mn2[i] for i in range(len(mn1))]
        y1_sq = [mn1[i] ** 2 for i in range(len(mn1))]
        y2_sq = [mn2[i] ** 2 for i in range(len(mn1))]
        y1_SquareSum = sum(y1_sq)
        y1_Sum = sum(average1)
        y2_SquareSum = sum(y1_sq)
        y2_Sum = sum(average2)
        sm_size = len(average1)
        product_sum = sum(product_min)
        formula_one = (sm_size * product_sum) - (y1_Sum * y2_Sum)
        formula_two = (((sm_size * y1_SquareSum) - (y1_Sum**2)) ** (1/2))
        formula_three = (((sm_size * y2_SquareSum) - (y2_Sum**2)) ** (1/2))
        try:
            cm_formulaFour = formula_one/(formula_two * formula_three)
        except:
            cm_formulaFour = 0.0
        min_corr = round(cm_formulaFour, 4)
        
        return [min_corr, max_corr, avg_corr, std_corr]
     
    
#Functions defining average_rainfall, maximum_rainfall, mn, standard_deviation
def average_rainfall(datas):
    average_list = []
    for i in datas:
        average = sum(i)/len(i)
        average_list.append(round(average,4))
    return (average_list)

def minimum_rainfall(datas):
    max_list = []
    for i in datas:
        maximum = max(i)
        max_list.append(maximum)
    return max_list

def standard_deviation(datas):
    stdev_list = []
    for x in datas:
        average = sum(x) / len(x)
        variance = sum((a-average)**2 for a in x) / len(x)
        std = (round((variance**(1/2)),4))
        stdev_list.append(std)
    return(stdev_list)

def maximum_rainfall(datas):
    all_Real_Values = [[value for value in x if value != 0.0] for x in datas]
    mn = []
    for a in all_Real_Values:
        if a == []:
            a.append(0.0)
    for a in all_Real_Values:
        minimum = min(a)
        mn.append(minimum)
    return mn
