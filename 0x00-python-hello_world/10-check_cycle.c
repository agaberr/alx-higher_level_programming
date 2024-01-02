#include "lists.h"

/**
 * check_cycle - if a singly-linked list has cycle
 * @list: linked list.
 *
 * Return: 1 if there is cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *front, *front_next;

	if (!list || !list->next)
		return (0);

	front = list->next;
	front_next = list->next->next;
	while (front && front_next && front_next->next)
	{
		if (front == front_next)
			return (1);

		front = front->next;
		front_next = front_next->next->next;
	}
	return (0);
}
