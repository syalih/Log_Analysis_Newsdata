# Log Analysis Newsdata
Log Analysis - Internal Reporting Tool | Udacity

# Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

# So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**Example:**
- "Princess Shellfish Marries Prince Handsome" — 1201 views
- "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
- "Political Scandal Ends In Political Scandal" — 553 views

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**Example:**
- Ursula La Multa — 2304 views
- Rudolf von Treppenwitz — 1985 views
= Markoff Chaney — 1723 views
- Anonymous Contributor — 1023 views

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

**Example:**
- July 29, 2016 — 2.5% errors
# Pre-requisites
1. Install VirtualBox
2. Install Vagrant
3. Download the Vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database file.

# Installing the Virtual Machine
We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

# Use a terminal
You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/).

# Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.


# Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is sucessfully installed, you will be able to run **"vagrant --version"** command in our terminal to see the version number. 
The shell prompt in your terminal may differ. Here the **"$"** sign is the shell prompt.

# Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

# Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command **"vagrant up"**. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When **"vagrant up"** is finished running, you will get your shell prompt back. At this point, you can run **"vagrant ssh"** to log in to your newly installed Linux VM! if Password ask default password for user: **"vagrant"** password: **"vagrant"**

**Errata:**
- **Note:** On some Windows systems, you will need to use **"winpty vagrant ssh"** instead of **"vagrant ssh"**

# The files for this course
Inside the VM, change directory to **"/vagrant"** and look around with **"ls"**.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: 

To load the data, **"cd"** into the **vagrant"" directory and use the command **"psql -d news -f newsdata.sql"**.
Here's what this command does:

- **"psql"** — the PostgreSQL command line program
- **"-d news"** — connect to the database named news which has been set up for you
- **"-f newsdata.sql"** — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

# Explore the data
Once you have the data loaded into your database, connect to your database using **"psql -d news"** and explore the tables using the **"\dt"** and - - **"\d"** table commands and **select** statements.

- **"\dt"** — display tables — lists the tables that are available in the database.
- **"\d"** table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

- The **authors** table includes information about the authors of articles.
- The **articles** table includes the articles themselves.
- The **log** table includes one entry for each time a user has accessed the site.

As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

# Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

- **db = psycopg2.connect("dbname=news")**
import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students ORDER BY name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()
