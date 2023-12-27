/**
 * file: ashculate.h
 * date created: 25-Dec-2023
 * date updated: 27-Dec-2023
 * author: Emmanuel Enchill
 *
 * description: this file contains the prototypes for all functions
 * of ASHCulator.
 */

#ifndef ASHCULATOR
#define ASHCULATOR

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* maximum length of a line */
#define BUFFER 1024

/* error messages */
#define ERR_INVALID_INPUT ":( Error: invalid input"
#define ERR_BAD_OPERAND ":( Error: invalid operand"
#define ERR_BAD_OPERATOR ":( Error: invalid operator"
#define ERR_ZERO_DIVISION ":( Error: division by zero"

/* error codes */
#define ERR_INVALID_INPUT_CODE -5
#define ERR_BAD_OPERAND_CODE -6
#define ERR_BAD_OPERATOR_CODE -7
#define ERR_ZERO_DIVISION_CODE -8

/* a structure to handle information */
typedef struct info
{
	/* result of computation */
	double result;

	/* error message */
	int err_code;
	int err_input; /* the input bug */
	char *err_msg;
	

	/* user input data */
	char *args;
	size_t len;
} info_t;

/* initializer for struct */
#define INFO_T_INIT {0.0, 0, 0, NULL, NULL, 0}

/* readLine function */
ssize_t readLine(info_t *);

/* function to parse the input */
int processInput(info_t *);

/* function to compute */
double computeResult(info_t *);

/* function to check digits of the decimal part of a number */
int checkDecDigits(double);

/* function to handle modulo division */
double handleModDiv(double, double);

#endif /* ASHCULATOR */
