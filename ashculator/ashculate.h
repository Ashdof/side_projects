#ifndef ASHCULATOR
#define ASHCULATOR

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* error messages */
#define ERR_INVALID_INPUT ":( Error: invalid input"
#define ERR_ZERO_DIVISION ":( Error: division by zero"
#define ERR_MISSING_PARENTHESIS ":( Error: missing closing parenthesis"

/* error codes */
#define ERR_INVALID_INPUT_CODE -5
#define ERR_ZERO_DIVISION_CODE -8
#define ERR_MISSING_PARENTHESIS_CODE -9

/* a structure to handle information */
struct var_data
{
	/* result of computation */
	int index;

	/* error message */
	int err_code;
	char err_input; /* the input bug */
	char *err_msg;

	/* user input data */
	char *args;
	size_t len;
};

typedef struct var_data INFO;

/* initializer for struct */
#define INFO_T_INIT {0, 0, 0, NULL, NULL, 0}

/* readLine function */
ssize_t readLine(INFO *);

/* function to parse the input */
int processInput(INFO *);

/* function to compute */
double computeResult(INFO *);

/* function to check digits of the decimal part of a number */
int checkDecDigits(double);

/* function to handle modulo division */
double handleModDiv(double, double);

/* function to handle addition and subtraction */
double handleAddSub(INFO *, const char *, int *);

/* function to handle a multiplication, division and modulo */
double handleMulDivMod(INFO *, const char  *, int *);

/* function to handle brackets */
double handleBrackets(INFO *, const char *, int *);

/* function to convert a sub-string to a double */
double handleSubstrToNumber(INFO *, const char *, int *);

/* function to evaluate and compute result */
double computeResult(INFO *);

#endif /* ASHCULATOR */
