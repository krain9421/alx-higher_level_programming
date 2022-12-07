#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_len - function that returns the
 * number of elements of a list_t list
 * @h: pointer to the list
 *
 * Return: number of elements in the list;
 */

int list_len(const listint_t *h)
{
	int count = 0;

	if (h == NULL)
	{
		return (count);
	}

	for (; h != NULL; h = h->next)
	{
		count++;
	}
	return (count);
}

/**
 * get_index - function returns the nth element
 * of a listint_t linked list
 * @head: pointer to linked list
 * @index: index of desired node
 *
 * Return: int
 * NULL if element doesn't exist
 */

int get_index(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *temp = head;

	while (temp != NULL)
	{
		if (i == index)
			return (temp->n);
		i++;
		temp = temp->next;
	}
	exit(1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singly linked list
 *
 * Return: 1 if list is a palindrome
 * 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int count = 0;
	int a = 0, b = 0, i = 0, flag = 0;

	current = *head;
	count = list_len(current);
	if (count == 0)
		return (1);

	for (i = 0; i < count; i++)
	{
		a = get_index(current, i);
		b = get_index(current, count - 1 - i);
		if (a != b)
		{
			flag = 1;
			break;
		}
	}

	if (flag)
		return (0);
	else
		return (1);
}
