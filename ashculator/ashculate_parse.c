#include "ashculate.h"

/**
 * processInput - parse input
 * @info: a pointer to a space in memory where a struct of data
 * information is stored.
 *
 * Return: Always 1
 */
int processInput(INFO *info)
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
		printf("%s [%c]\n", info->err_msg, info->err_input);
	else
	{
		int_part = (int) ans;
		dec_part = ans - int_part;

		state = checkDecDigits(dec_part);
		if (state == 1)
			printf(":) %f\n", ans);
		else
			printf(":) %d\n", int_part);
	}

	info->index = 0;
	info->err_code = 0;
	info->err_input = 0;
	info->err_msg = NULL;

	return (1);
}

/**
 * handleBrackets - handle brackets
 * @info: a pointer to a space in memory where a struct of data is
 * stored
 * @args: a pointer to the line of input
 * @index: a pointer to the index of the value
 *
 * Return: result of computation or a converted number
 */
double handleBrackets(INFO *info, const char *args, int *index)
{
	double result;

	if (args[*index] == '(')
	{
		(*index)++;

		result = handleAddSub(info, args, index);

		if (args[*index] == ')')
		{
			(*index)++;
			return (result);
		}
		else
		{
			info->err_code = ERR_MISSING_PARENTHESIS_CODE;
			info->err_input = ')';
			info->err_msg = ERR_MISSING_PARENTHESIS;

			return (0);
		}
	}
	else
		return (handleSubstrToNumber(info, args, index));
}

/**
 * computeResult - evaluate and compute result
 * @info: a pointer to a space in memory where a struct of data
 * is stored
 *
 * Return: result of computation
 */
double computeResult(INFO *info)
{
	char *p = info->args;

	for (; *p != '\0'; p++)
	{
		if (*p == ' ')
		{
			info->err_code = ERR_INVALID_INPUT_CODE;
			info->err_input = *p;
			info->err_msg = ERR_INVALID_INPUT;

			return (1);
		}
	}

	return (handleAddSub(info, info->args, &info->index));
}

/**
 * handleSubstrToNumber - convert a sub-string to a double
 * @info: a pointer to a space in memory where a struct of data is
 * stored
 * @args: a pointer to the line of input
 * @index: a pointer to the index of the value
 *
 * Return: the converted value
 */
double handleSubstrToNumber(INFO *info, const char *args, int *index)
{
	double result = 0.0, frac = 0.1;
	int isNegative = 0;

	if (args[*index] == '-')
	{
		isNegative = 1;
		(*index)++;
	}

	/* handle digits before the dot */
	while (isdigit(args[*index]))
	{
		result = result * 10.0 + (args[*index] - '0');
		(*index)++;
	}

	/* handle digits after the dot in a floating point number */
	if (args[*index] == '.')
	{
		(*index)++;
		while (isdigit(args[*index]))
		{
			result += (args[*index] - '0') * frac;
			frac /= 10.0;
			(*index)++;
		}
	}

	if (isNegative)
		result = -result;

	if (args[*index] == '(')
		result *= handleBrackets(info, args, index);

	return (result);
}
