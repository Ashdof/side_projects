/**
 * file: ashculate_parse.c
 * date created: 25-Dec-2023
 * date updated: 27-Dec-2023
 * author: Emmanuel Enchill
 *
 * description: this file contains functions that checks for errors
 * in the data supplied by the user
 *
 * Functions:
 * @processInput
 * @computeResult
 * @checkDecDigits
 * @handleModDiv
 *
 */

#include "ashculate.h"

/**
 * processInput - parse input
 * @info: a pointer to a space in memory where a struct of data
 * information is stored.
 *
 * description: this function takes the input data, checks for
 * invalid input(non-digits and missing operation sign) and
 * invokes other functions to execute the arithmetic computation
 *
 * Return: Always 1
 */
int processInput(info_t *info)
{
	double ans, dec_part;
	int int_part, state;
	char *p;

	/* get rid of the newline character */
	for (p = info->args; *p != '\0'; p++)
	{
		if (*p == '\n')
			*p = '\0';
	}

	if (strcmp(info->args, "exit") == 0)
		return (0);

	ans = computeResult(info);
	if (info->err_code != 0)
	{
		printf("%s\n", info->err_msg);
		return (1);
	}

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
 * @info: a pointer to a space in memory where a struct of data
 * information is stored
 *
 * Return: the results of the computation
 */
double computeResult(info_t *info)
{
	double operand, result = 0.0;
    	char op = '+', *line = info->args;
    	int i = 0;

    	while (line[i] != '\0') {
		if (line[i] == '+' || line[i] == '-' || line[i] == '*' || line[i] == '/' || line[i] == '%')
		{
			op = line[i];
			i++;
		}

		if (isdigit(line[i]) || (line[i] == '-' && !isdigit(line[i - 1])))
		{
			if (sscanf(line + i, "%lf", &operand) != 1) {
				info->err_code = ERR_BAD_OPERAND_CODE;
				info->err_msg = ERR_BAD_OPERAND;
				return (0);
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
						info->err_code = ERR_ZERO_DIVISION_CODE;
                        			info->err_msg = ERR_ZERO_DIVISION;
						return (0);
                    			}
                    			result /= operand;
                    			break;
				case '%':
					if (operand == 0.0)
					{
						info->err_code = ERR_ZERO_DIVISION_CODE;
						info->err_msg = ERR_ZERO_DIVISION;
						return (0);
					}

					result = handleModDiv(result, operand);
					break;
                		default:
					info->err_code = ERR_BAD_OPERATOR_CODE;
					info->err_msg = ERR_BAD_OPERATOR;
					return (0);
            		}

            		while (isdigit(line[i]) || line[i] == '.') {
                		i++;
            		}
        	}
		else
		{
			info->err_code = ERR_INVALID_INPUT_CODE;
			info->err_msg = ERR_INVALID_INPUT;
			return (0);
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
