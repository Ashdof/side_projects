#include "ashculate.h"

/**
 * handleAddSub - implement addition and subtraction computations
 * @info: a pointer to a space in memory where a struct of data is
 * stored
 * @args: a pointer to the line of input
 * @index: a pointer to the index of the value
 *
 * Return: result of computation
 */
double handleAddSub(INFO *info, const char *args, int *index)
{
	double operand, ans;
	char op;

	ans = handleMulDivMod(info, args, index);

	while (args[*index] == '+' ||
	       args[*index] == '-')
	{
		op = args[(*index)++];
		operand = handleMulDivMod(info, args, index);
		if (op == '+')
			ans += operand;
		else
			ans -= operand;
	}

	return (ans);
}

/**
 * handleMulDivMod - implement multiplication, division and modulo
 * computations
 * @info: a pointer to a space in memory where a struct of data is
 * stored
 * @args: a pointer to the line of input
 * @index: a pointer to the index of the value
 *
 * Return: result of computation
 */
double handleMulDivMod(INFO *info, const char *args, int *index)
{
	double operand, ans;
	char op;

	ans = handleBrackets(info, args, index);

	while (args[*index] == '*' ||
	       args[*index] == '/' ||
	       args[*index] == '%')
	{
		op = args[(*index)++];
		operand = handleBrackets(info, args, index);

		switch (op)
		{
			case '*':
				ans *= operand;
				break;
			case '/':
				if (operand == 0.0)
				{
					info->err_code = ERR_ZERO_DIVISION_CODE;
					info->err_input = '0';
					info->err_msg = ERR_ZERO_DIVISION;

					return (0);
				}

				ans /= operand;
				break;
			case '%':
				if (operand == 0.0)
				{
					info->err_code = ERR_ZERO_DIVISION_CODE;
					info->err_input = '0';
					info->err_msg = ERR_ZERO_DIVISION;

					return (0);
				}

				ans = handleModDiv(ans, operand);
				break;
			default:
				break;
		}
	}

	return (ans);
}
