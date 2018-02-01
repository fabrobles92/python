import webapp2
import cgi

form="""
<form method="post"> 
	Whats is your birthday?
	<br>
	<label>Month <input type="text" name="month" value="%(month)s"></label>
	<label>Day <input type="text" name="day" value="%(day)s"></label>
	<label>Year <input type="text" name="year" value="%(year)s"> </label>
	<div style="color: red">%(error)s</div>
	<input type="submit">
</form> 
"""

months = ['January',
		  'February',
		  'March',
		  'April',
		  'May',
		  'June',
		  'July',
		  'August',
		  'September',
		  'October',
		  'November',
		  'December']
		  
month_abbvs = dict((m[:3].lower(),m) for m in months)


			
class MainPage(webapp2.RequestHandler):
	def write_form(self,error="",month="",day="",year=""):
		self.response.out.write(form % {"error": error,
										"month": escape_html(month),
										"day": escape_html(day),
										"year":escape_html(year)})
		
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.write_form()
		
	def post(self):
		month = self.request.get("month")
		day = self.request.get("day")
		year = self.request.get("year")
		
		user_month = valid_month(month)
		user_day = valid_day(day)
		user_year = valid_year(year)

	
		if not (user_month and user_day and user_year):
                    self.write_form("Invalid!",month,day,year)
		else:
                    self.response.out.write("Info OK!")

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)


def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)
		
def valid_day(day):
	if day.isdigit():
		 daynumber = int(day)
		 if daynumber >= 1 and daynumber <= 31:
				return daynumber
				
def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year >= 1900 and year <= 2020:
			return year
			
def escape_html(s):
	if s :
		cgi.escape(s, quote = True)