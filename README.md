# recommendersystem
Recommendation System to recommend top books from the dataset  

The "recom.py" is the main program code.  
The dataset is also added here under the name "data_books.csv". Its a csv (comma separated value) file which contains 3 fields namely Reviewer, Book and Rating (from 1 to 10), separated by commas.  
Pearson Correlation is used to find the correlation or similarity between two books. It is present in SciPy library and can be imported into code by using "from scipy.stats import pearsonr"; but the main problem in this function is that it cannot handle ZeroDivisionError. So I have included my header file named "function.py" ehich overcome this problem.  
