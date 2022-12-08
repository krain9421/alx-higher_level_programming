#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* print_dlistint - function that prints all the
* elements of a dlistint_t list
* @h: pointer to the list
*
* Return: number of nodes in the list;
*/

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	if (h == NULL)
	{
		return (count);
	}

	for (; h != NULL; h = h->next)
	{
		/*if (h->str == NULL)*/
			/*printf("[0] (nil)\n");*/
		printf("%d\n", h->n);

		count++;
	}
	return (count);
}

