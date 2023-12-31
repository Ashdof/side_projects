#include "ashculate.h"

/**
 * checkDecDigits - check decimal digits
 * @value: a value with floating point numbers
 *
 * Return: 1 if digit is greater than 0, or 0 if all digits
 * are 0
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
