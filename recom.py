from __future__ import division
import pandas as pd
import numpy as np
import time
from function import *
from scipy.stats import pearsonr

def nl():
	print "\n"

def read_data():
	data = pd.read_csv("data_books.csv", sep = ",", header=None, names=['Reviewer', 'Book', 'Rating'])
	unique_reviewer = list(set(data.Reviewer))
	unique_book = list(set(data.Book))
	print "There are %d rows in this dataframe" %len(data)
	print "There are %d unique books in this dataframe" %len(unique_book)
	print "There are %d unique reviewer in this dataframe" %len(unique_reviewer)
	var = (len(unique_book) * len(unique_reviewer))
	sparsity = (len(data) / var) * 100
	print "The sparsity of the database is %.7f %%" %sparsity
	return data, unique_book

def top_books1(d, n):
	print "Displaying top "+str(n)+" most reviewd books:\n"
	top_books = pd.value_counts(d.Book)
	return top_books.head(n)

def top_reviewers(d, n):
	print "Displaying top "+str(n)+" reviewers:\n"
	top_reviewers = pd.value_counts(d.Reviewer)
	return top_reviewers.head(n)

def get_book_reviews(title, common_reviewers):
    	mask = (data.Reviewer.isin(common_reviewers)) & (data.Book==title)
    	reviews = data[mask].sort_values('Reviewer')
    	reviews = reviews[reviews.Reviewer.duplicated()==False]
    	return reviews

def calculate_correlation(book1, book2):
	book_1_reviewers = data[data.Book == book1].Reviewer
    	book_2_reviewers = data[data.Book == book2].Reviewer
    	common_reviewers = set(book_1_reviewers).intersection(book_2_reviewers)
	book_1_reviews = get_book_reviews(book1, common_reviewers)
	book_2_reviews = get_book_reviews(book2, common_reviewers)
	return pearsonr1(book_1_reviews.Rating, book_2_reviews.Rating)

def common_reviewers(book1, book2):
	book_1_reviewers = data[data.Book == book1].Reviewer
	book_2_reviewers = data[data.Book == book2].Reviewer
	common_reviewers = set(book_1_reviewers).intersection(book_2_reviewers)
	return common_reviewers

#Actual Recommendation System
def top_books(n):
	most_reviewed_books = pd.DataFrame({'count' : data.groupby(["Book"]).size()})\
				   .reset_index().sort_values(['count'],ascending = False)
	top_books = []
	for i in most_reviewed_books.Book[0:n]:
	    top_books.append(i)
	return top_books

def recommended_books(book, top_books):
	results = []
	for b in top_books:
	    if book!=b:
		p = calculate_correlation(book, b)
		if p < 0:
			continue
		comm_rev = len(common_reviewers(book, b))
		if comm_rev <= 0:
			return 0
		results.append((b, p, comm_rev))
	cols = ["Book", "Correlation", "Common_Reviewers"]
	results = pd.DataFrame(results, columns=cols).sort_values(['Correlation'],ascending = False)
	return results

data, unique_book = read_data()
nl()

n1 = input("Enter the number of top reviewed books to be displayed:\t")
if(n1 > 1 and n1 < 383852):
	tb = top_books1(data, n1)
	print tb
else:
	print "Number entered doesn't satisfy the limit condition!"
	print "Considering default value i.e. 20"
	tb = top_books1(data, 20)
	print tb
nl()

n2 = input("Enter the number of top reviewers to be displayed:\t")
if(n2 > 0 and n2 < 383852):
	print top_reviewers(data, n2)
else:
	print "Number entered doesn't satisfy the limit condition!"
	print "Considering default value i.e. 20"
	print top_reviewers(data, 20)
nl()

print "Pearson Correlation Coefficient between 2 books:->"
b1 = raw_input("Enter the name of the first book:\t")
b2 = raw_input("Enter the name of the second book:\t")
if(b1 != b2):
	print "Pearson Correlation Coefficient between '",b1,"' and '",b2,"' =",calculate_correlation(b1, b2)
	common = common_reviewers(b1, b2)
	print "%d people have reviewed these 2 books" %len(common)
	print common
else:
	print "Pearson Correlation Coefficient between same book is always 1.0"
nl()

start_time = time.time()
tb = top_books(n1)
print "Recommended books for users who liked a given book:->"
b = raw_input("Enter the name of the book for which related books are to be shown:\t")
print "Books which are most reviewd and which are some what similar to '",b,"' so that they can be recommended to user who liked book '",b,"'"
rb = recommended_books(b, tb)
print rb
print "%s seconds required to complete the computation" %(time.time() - start_time)

f = open('output.txt', 'wb')
print >> f, rb
f.close()
print "Result is also available in 'output.txt' file"
