import graphene
from graphene_django import DjangoObjectType

from tickets.models import Ticket


class TicketType(DjangoObjectType):
    class Meta:
        model = Ticket


class Query(graphene.ObjectType):
    tickets = graphene.List(TicketType)

    def resolve_tickets(self, info, **kwargs):
        return Ticket.objects.all()


class CreateTicket(graphene.Mutation):
    #Defined for learning purpose
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    reported_by = graphene.String()
    assigned_to = graphene.String()
    status = graphene.String()

    class Arguments:
        #actual definition
        title = graphene.String()
        description = graphene.String()
        reported_by = graphene.String()
        assigned_to = graphene.String()
        status = graphene.String()

    def mutate(self, info, title, description, reported_by, assigned_to, status):
        ticket = Ticket(title=title, description=description, reported_by=reported_by, assigned_to=assigned_to, status=status)
        #Saving the ticket
        ticket.save()

        return CreateTicket(
            id=ticket.id,
            title=ticket.title,
            description=ticket.description,
            reported_by=ticket.reported_by,
            assigned_to=ticket.assigned_to,
            status=ticket.status,
        )

class UpdateTicket(graphene.Mutation):
 
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    reported_by = graphene.String()
    assigned_to = graphene.String()
    status = graphene.String()

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        reported_by = graphene.String()
        assigned_to = graphene.String()
        status = graphene.String()

    def mutate(self, info, id, title, description, reported_by, assigned_to, status):
        ticket = Ticket(id=id,  title=title, description=description, reported_by=reported_by, assigned_to=assigned_to, status=status)
        ticket.save()

        return UpdateTicket(
            id=ticket.id,
            title=ticket.title,
            description=ticket.description,
            reported_by=ticket.reported_by,
            assigned_to=ticket.assigned_to,
            status=ticket.status,
        )

class DeleteTicket(graphene.Mutation):

    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    reported_by = graphene.String()
    assigned_to = graphene.String()
    status = graphene.String()

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        reported_by = graphene.String()
        assigned_to = graphene.String()
        status = graphene.String()

    def mutate(self, info, id, title, description, reported_by, assigned_to, status):
        ticket = Ticket(id=id,  title=title, description=description, reported_by=reported_by, assigned_to=assigned_to, status=status)
        ticket.delete()

        return DeleteTicket(
            id=ticket.id,
            title=ticket.title,
            description=ticket.description,
            reported_by=ticket.reported_by,
            assigned_to=ticket.assigned_to,
            status=ticket.status,
        )


class Mutation(graphene.ObjectType):
    create_ticket = CreateTicket.Field()
    update_ticket = UpdateTicket.Field()
    Delete_ticket = DeleteTicket.Field()
