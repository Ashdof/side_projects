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
	float ans;
	__attribute__((unused)) int int_part, dec_part;
	char *p;

	/* get rid of the newline character */
	for (p = line; *p != '\0'; p++)
	{
		if (*p == '\n')
			*p = '\0';
	}

	ans = computeResult(line);
	printf(":) %.2f\n", ans);

	return (1);
}

/**
 * computeResult - execute arithmetic computation
 * @line - a pointer to the input data
 *
 * Return: the results of the computation
 */
float computeResult(const char *line)
{
	double operand, result = 0.0;
    	char op = '+';
    	int i = 0;

    	while (line[i] != '\0') {
        	if (isdigit(line[i]) || (line[i] == '-'
		    && (i == 0 || !isdigit(line[i - 1]))))
		{
			if (sscanf(line + i, "%lf", &operand) != 1) {
				ERR_BAD_OPERAND(operand);
				break;
				/*exit(EXIT_FAILURE);*/
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
						break;
                        			/*exit(EXIT_FAILURE);*/
                    			}
                    			result /= operand;
                    			break;
                		default:
					ERR_BAD_OPERATOR(line[i]);
					break;
                    			/*exit(EXIT_FAILURE);*/
            		}

            		while (isdigit(line[i]) || line[i] == '-' || line[i] == '.') {
                		i++;
            		}
        	}
		else if (line[i] == '+' || line[i] == '-' || line[i] == '*' || line[i] == '/')
		{
            		op = line[i];
            		i++;
        	}
		else
		{
			ERR_INPUT(line[i]);
			break;
           	 	/*exit(EXIT_FAILURE);*/
        	}
	}

	return (result);
}
