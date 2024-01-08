#include "lists.h"

/**
 * check_palindrome - check palindrome in sigly linked list
 * @left: head to linked list
 * @right: end of the linked list
 *
 * Return: 1 if palindrome, 0 otherwise
 **/

int check_palindrome(listint_t **left, listint_t *right)
{
	int pal = 0;

	if (!right)
		return (1);

	pal = ((*left)->n == right->n && check_palindrome(left, right->next));
	*left = (*left)->next;

	return (pal);
}

/**
 * is_palindrome - check if linked list is a palindrome
 * @head: head to linked list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);

	return (check_palindrome(head, *head));
}
