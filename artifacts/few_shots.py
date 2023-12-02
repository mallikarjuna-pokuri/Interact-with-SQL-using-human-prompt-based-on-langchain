few_shots = [
    {'Question' : "What is the total bill of the patient Robinson",
     'SQLQuery' : """
     select sum(qty*unitprice) 
     from bill inner join billitem on bill.billno = billitem.billno 
     inner join patient on patient.patientid = bill.patientid 
     where patient.name = "Robinson" 
     """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "85000"},
    {'Question': "Who supervises nurse Wilkie",
     'SQLQuery':"""select staffname from staff 
     where staffno in 
     (select s1.nurseno from supervises s1inner join supervises s2 
     on s1.relid = s2.relid inner join staff on staff.staffno = s2.nurseno 
     where s1.isupervisor>s2.issupervisor and staff.staffname = "Wilkie")""",
     'SQLResult': "Result of the SQL query",
     'Answer': "Colman supervises Wilkie"},
    {'Question': "Who is the doctor of patient Bell and tell me about the doctor" ,
     'SQLQuery' : """
     select patient.name,staffname,specialty,docposition from patient inner join doctor on patient.doctorno = doctor.staffno 
    inner join staff on staff.staffno = doctor.staffno
    where name = "Bell"
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Patient Name is Bell and the doctor name is Ansell with position as consultant and specialty in Orthopedic"} ,
    {'Question': "Tell me about the nurse who takes care of the patient of James",
     'SQLQuery' : """
     select n.wardno, s.staffname, d.specialty
     from patient p
            inner join doctor d on d.staffno = p.doctorno
            inner join nurse n on p.wardno = n.wardno
            inner join staff s on s.staffno = n.staffno
            where name = "James"
     """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "Total of 8 nurses takes care of the ward w4 with the names of two of them are Peters, Locke"
     },
    {'Question': "How much is total amount of money still needs to be paid by patients",
     'SQLQuery' : """
     select sum(qty*unitprice) from rcptdetail r
        right join billitem b
        on r.billno = b.billno
        and r.lineno = b.lineno
        where r.billno is null
 """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "72000.50"
    }
]

mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """
