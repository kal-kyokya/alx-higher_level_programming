#include "lists.h"

/**
 * insert_node - Insert a node accordingly in a sorted SLL.
 * @head: Address of the head pointer.
 * @number: Integer value of the node to be inserted.
 *
 * Return: A pointer to the inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	current = *head;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	while (current != NULL)
	{
		if (current->n >= new_node->n && current == *head)
		{
			*head = new_node;
			new_node->next = current;
			break;
		}
		else if (current->n <= new_node->n && current->next == NULL)
		{
			new_node->next = NULL;
			current->next = new_node;
			break;
		}
		else if (current->n <= new_node->n && new_node->n <= current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			break;
		}
		current = current->next;
	}

	return (new_node);
}
