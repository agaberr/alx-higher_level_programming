#include "lists.h"

/**
 * check_cycle - if a singly-linked list has cycle
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
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
