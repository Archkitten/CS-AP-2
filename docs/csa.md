# CSA

{% include csa_nav.html %}

## Replit Runtime:

<iframe src="https://replit.com/@ArchHuang/CS-AP-A?lite=true" width="800px" height="450px"></iframe>

In order to update:
1. Open in Replit
2. Project Tab → Version Control
3. 'pull' button

## .replit
```
language="bash"
run="cd src && javac csa/*.java && java csa/Main && rm csa/**/*.class"
```

## Makefile (by MZ)
```
run: build execute

build:
	find -name *.java > sources.txt
	javac -d bin @sources.txt

execute:
	java -cp ./bin csa/Main

clean:
	rm -rf ./bin/*
	rm sources.txt
```
* make - updates and runs program
* make run - updates and runs program
* make build - updates program
* make execute - runs program
* make clean - remove all .class files
