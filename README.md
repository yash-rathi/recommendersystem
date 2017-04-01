# recommendersystem
Recommendation System to recommend top books from the dataset  

  
## Introduction
The __recom.py__ is the main program code.  
  
The dataset is also added here under the name __data_books.csv__. Its a csv (comma separated value) file which contains 3 fields namely __Reviewer__, __Book__ and __Rating__ (from 1 to 10), separated by commas.  
  
Pearson Correlation is used to find the correlation or similarity between two books. It is present in __SciPy__ library under module name __stats__ by name __pearsonr__ function; but the main problem in this function is that it cannot handle ZeroDivisionError. So I have included my header file named __function.py__ which overcome this problem.  

  
## Prerequisites
The following libraries or modules are required to run this code and how to install them  
1) **pandas**  
pandas is a software library written for the Python programming language for data manipulation and analysis.
```
$ pip install pandas
```  
2) **future**  
future is the missing compatibility layer between Python 2 and Python 3. It allows you to use a single, clean Python 3.x-compatible codebase to support both Python 2 and Python 3 with minimal overhead.  
Here, we are using __ future division__ statement which changes the normal division operation.  
```
$ pip install future
```  
3) **numpy**  
NumPy is the fundamental package for scientific computing with Python.
```
$ pip install numpy
```

  
## Execution
The code can be run by simply writing following command in the terminal
```
$ python recom.py
```

  
## Built with
* **Python**

  
## Author
* **Yash Rathi** - [yash-rathi](https://github.com/yash-rathi)

  
## Acknowledgments
* [**Mickael Le Gal**](https://github.com/mickaellegal/)
