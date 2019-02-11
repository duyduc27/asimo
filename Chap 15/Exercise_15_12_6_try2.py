# Exercise 15.12.6
from unit_tester import test
class SMS_store:
    """ Simulate inbox or outbox features of a cellphone """
    def __init__(self):
        """ Create initializer of class """
        self.messages = []
    def __str__(self):
        return "{0}".format(self.messages)

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Simulate a new message arrivad """
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its
        # has_been_viewed status is set False.
        self.from_number  = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS  = text_of_SMS
        return self.messages.append((False, self.from_number, self.time_arrived, self.text_of_SMS))
        # We have 2 parentheses because the form of a message

    def message_count(self):
        """ Return the number of sms messages in my_inbox """
        return len(self.messages)

    def get_unread_indexes(self):
        """ Return list of indices of all not-yet-viewed SMS messages """
        result = [] # Set initial result
        for i,v in enumerate(self.messages):
            if v[0] == False:
                result.append(i)
        return result

    def get_message(self, i):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
        if i < 0 or i >= len(self.messages):
            return None
        else:
            read_msg = (True,) + self.messages[i][1:] # Create a new state of this msg
            self.messages[i] = read_msg
            return self.messages[i]

    def delete(self, i):
        """ Delete msg at i index """
        del self.messages[i]
        return self.messages

    def clear(self):
        """ Delete all messages from inbox """
        self.messages = []
        return self.messages

my_inbox = SMS_store()

my_inbox.add_new_arrival('0123', '7:00 AM', "Haven't you wake up yet, honey?")
my_inbox.add_new_arrival('1234', '7:05 AM', 'We have a important meeting, bro!')

test(my_inbox.messages == [(False, '0123', '7:00 AM', "Haven't you wake up yet, honey?")
, (False, '1234', '7:05 AM', 'We have a important meeting, bro!')])

test(my_inbox.message_count() == 2)
test(my_inbox.get_unread_indexes() == [0, 1])

test(my_inbox.get_message(1) == (True, '1234', '7:05 AM', 'We have a important meeting, bro!'))
test(my_inbox.get_message(2) == None)

my_inbox.delete(1)
test(my_inbox.messages == [(False, '0123', '7:00 AM', "Haven't you wake up yet, honey?")])

test(my_inbox.clear() == [])