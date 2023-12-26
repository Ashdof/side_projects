/**
 * file: ashculate_parse.c
 * date created: 25-Dec-2023
 * date updated: 25-Dec-2023
 * author: Emmanuel Enchill
 *
 * description: this file contains functions that checks for errors
 * in the data supplied by the user
 *
 * Functions:
 * @processInput
 * @computeResult
 */

#include "ashculate.h"

/**
 * processInput - parse input
 * @line: a pointer to the input data
 *
 * description: this function takes the input data, checks for
 * invalid input(non-digits and missing operation sign) and
 * invokes other functions to execute the arithmetic computation
 *
 * Return: Always 1
 */
int processInput(char *line)
{
	double ans, dec_part;
	int int_part, state;
	char *p;

	/* get rid of the newline character */
	for (p = line; *p != '\0'; p++)
	{
		if (*p == '\n')
			*p = '\0';
	}

	ans = computeResult(line);
	int_part = (int) ans;
	dec_part = ans - int_part;

	state = checkDecDigits(dec_part);
	if (state == 1)
		printf(":) %f\n", ans);
	else
		printf(":) %d\n", int_part);

	return (1);
}

/**
 * computeResult - execute arithmetic computation
 * @line - a pointer to the input data
 *
 * Return: the results of the computation
 */
double computeResult(const char *line)
{
	double operand, result = 0.0;
    	char op = '+';
    	int i = 0;

    	while (line[i] != '\0') {
		if (line[i] == '+' || line[i] == '-' || line[i] == '*' || line[i] == '/' || line[i] == '%')
		{
			op = line[i];
			i++;
		}

		if (isdigit(line[i]) || (line[i] == '-' && !isdigit(line[i - 1]) && line[i] != '.'))
		{
			if (sscanf(line + i, "%lf", &operand) != 1) {
				ERR_BAD_OPERAND(operand);
				result = 0.0;
				return (result);
			}

			switch (op) {
                		case '-':
                    			result -= operand;
                    			break;
                		case '+':
                    			result += operand;
                    			break;
                		case '*':
                    			result *= operand;
                   			break;
                		case '/':
                    			if (operand == 0.0) {
                        			printf(ERR_ZERO_DIVISION);
						result = 0.0;
						return (result);
                    			}
                    			result /= operand;
                    			break;
				case '%':
					if (operand == 0.0)
					{
						printf(ERR_ZERO_DIVISION);
						result = 0.0;
						return (result);
					}

					result = handleModDiv(result, operand);
					break;
                		default:
					ERR_BAD_OPERATOR(line[i]);
					result = 0.0;
					return (result);
            		}

            		while (isdigit(line[i]) || line[i] == '.') {
                		i++;
            		}
        	}
		else
		{
			ERR_INPUT(line[i]);
			result = 0.0;
			return (result);
        	}
	}

	return (result);
}

/**
 * checkDecDigits - check decimal digits
 * @value: number with floating point values
 *
 * Return: 1 if a digit is greater 0, 0 if all digits are 0
 */
int checkDecDigits(double value)
{
	while (value != (int) value)
	{
		value *= 10;
		if (value > 0)
			return (1);
	}

	return (0);
}

/**
 * handleModDiv - handle modulo division
 * @value: the value to be divided
 * @operand: the number to divide the value
 *
 * description: this function handles modulo division
 *
 * Return: the result of the division
 */
double handleModDiv(double value, double operand)
{
	double quo, div, ans;

	quo = value / operand;
	div = (double)((long) quo);
	ans = value - operand * div;

	return (ans);
}
