from pyping.core import Response


def process_results(nicknames, responses):
    print_to_console(nicknames, responses)


def print_to_console(nicknames, responses):
    for i in range(len(responses)):
        print "response from \"{}\" ({}):".format(nicknames[i][0], nicknames[i][1])

        r = responses[i]

        if not isinstance(r, Response):
            print "an error occurred: {}\n".format(r)
            return

        print "packet loss: {}".format(r.packet_lost)
        print "Average ping time: {}ms, min: {}ms, max: {}ms".format(r.avg_rtt, r.min_rtt, r.max_rtt)
        print "\n"
