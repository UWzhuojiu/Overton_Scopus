# Scopus_Databrick_Notebook
In this folder, there are notebooks from databricks platform where we can use the scopus data from ICSR lab.
And also some data csv file we manually tagged or processed after export from these notebook which we used in other notebooks.

## affiliation parent
Data like "A university" and "Department of B in A university" both exists in Scopus affiliation/institution list. Thus we need to get the parent of these affiliated organization.

Affiliation_parent_1.ipynb and affiliation_parent_2.ipynb both used tables in Scopus to help get the parent data. The result of Affiliation_parent_1.ipynb is restored in Databrick. And affiliation_parent_2.ipynb's result was exported and we mannually tagged the result. The mannually tagged result is the file affiliation_parent_2.csv.

affiliation_parent_integration.ipynb is used to comnine the result of two notebooks above. 