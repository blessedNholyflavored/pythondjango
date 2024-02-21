#! /usr/bin/env python3

def parsing(word : str):
    part = word.split("=")
    result = dict((value.strip().split(":") for value in part[1].split(", ")))
    result["name"] = part[0].strip()
    return result



def read_file():
    HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>periodic_table</title>
    <style>
        table{{
        border-collapse: collapse;
        }}
        h4 {{
        text-align: center;
        }}
        ul {{
        list-style:none;
        padding-left:0px;
        }}
    </style>
    </head>
    <body>
    <table>
        {body}
    </table>
    </body>
    </html>
    """

    TEMPLATE = """
        <td style="border: 2px solid black; padding:20px">
            <h4>{name}</h4>
            <ul>
            <li>No {number}</li>
            <li>{small}</li>
            <li>{molar}</li>
            <li>{electron} electron</li>
            </ul>
        </td>
    """
    body = "<tr>"
    with open("periodic_table.txt",'r') as data_file:
            periodic_table = [(parsing(line)) for line in data_file.readlines()]
            # periodic_table.write('<tr>\n')
            data_file.close()
            
            # il faut chopper la position des elements pr les classer sa race
            position = 0 

            for dict in periodic_table:
                if position > int(dict["position"]):
                    body += "    </tr>\n    <tr>"
                    position = 0
                for _ in range(position, int(dict["position"]) - 1):
                    body += "      <td></td>\n"
                position = int(dict["position"])
                body += TEMPLATE.format(
                    name=dict["name"],
                    number=dict["number"],
                    small=dict["small"],
                    molar=dict["molar"],
                    electron=dict["electron"],
                )
            # parsing(data)
            # print(periodic_table)

            body += "    </tr>\n"
            html = open("periodic_table.html", "w")
            html.write(HTML.format(body=body))
            html.close()
        # print(filee)


if __name__ == '__main__':
    read_file()




#creating a text file with the command function "x"
