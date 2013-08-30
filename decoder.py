#*-* coding: utf8 *-*

from email.header import decode_header

class Decoder:
    @staticmethod
    def get_encodig(enc):
        if enc:
            return enc
        else:
            return 'utf8'

    @staticmethod
    def decode(header):
        head = {}
        head['To'] = ""
        head['From'] = ""
        head['Subject'] = ""
        head['Date'] = ""
        lines = header.splitlines()
        to_del = []
        for i, l in enumerate(lines):
            if not ":" in l:
                lines[i-1] += ' ' + l
                to_del.append(i)
        for i in to_del[::-1]:
            del(lines[i])
        for l in lines:
            line = l.split(':', 1)
            dec = decode_header(line[1].replace('"',''))
            head[line[0]] = " ".join([i[0].decode(Decoder.get_encodig(i[1])).strip() for i in dec])
        return head
