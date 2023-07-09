from fpdf import FPDF

# Here I extend the class FDF with methods for header and footer
class Shirtificate(FPDF):
    def header(self):

        self.set_font("courier", "B", 48)         # Setting font: courier bold 22
        self.set_text_color(27, 71, 171)    # Setting colour: a shade of purple

        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: courier italic 8
        self.set_font("courier", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def main():
    pdf_with_text(input("What's your name? "))


def pdf_with_text(name):
    #first, create sentence to that we can have the part took CS50
    sentence = name + " took CS50"


    #PDF should be A4, which is 210mm wide by 297mm tall.
    # I call the extended PDF instead of  FPDF to access header and footer
    pdf = Shirtificate(format="A4", orientation="P")
    pdf.add_page()


    # adds image centered horizontally
    pdf.image("shirtificate.png", x=pdf.x/2, y= 60, w=200)

    #prepares the font to write user name
    pdf.set_text_color(255, 255, 255) # set to white
    pdf.set_font("courier", "B", 24) # set font I like
    pdf.set_x(pdf.x/2) #set coordinates for x, centering horizontally
    pdf.set_y(120) # set coordinates for y
    pdf.cell(0, 10, sentence, align='C') # ads the user name

    # generates PDF based on user name
    #pdf.output("00_simple_"+ name +".pdf")

    pdf.output("shirtificate.pdf") # saves as this name based on assignment





if __name__ == "__main__":
    main()