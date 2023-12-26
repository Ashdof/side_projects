/**
 * file: ashculate.h
 * date created: 25-Dec-2023
 * date updated: 25-Dec-2023
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

/* error messages */
#define ERR_INPUT(n) printf(":( Error: invalid input [%c]\n", (n))
#define ERR_BAD_OPERAND(n) printf(":( Error: invalid operand [%f]\n", (n))
#define ERR_BAD_OPERATOR(n) printf(":( Error: invalid operator [%c]\n", (n))
#define ERR_ZERO_DIVISION ":( Error: division by zero\n"

/* readLine function */
ssize_t readLine(char **, size_t);

/* function to parse the input */
int processInput(char *);

/* function to compute */
double computeResult(const char *);

/* function to check digits of the decimal part of a number */
int checkDecDigits(double);

/* function to handle modulo division */
double handleModDiv(double, double);

#endif /* ASHCULATOR */
