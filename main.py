import webapp2

form="""
<form method="post"> 
	Whats is your birthday?
	<br>
	
	<label> Month
		<input type="text" name"month">
	</label>
	
	<label> Day
		<input type="text" name"day">
	</label>
	
	<label> Year
		<input type="text" name"year"> 
	</label>
	
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
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
		
    def post(self):
	user_month = valid_month(self.request.get("month"))
	user_day = valid_day(self.request.get("day"))
	user_year = valid_year(self.request.get("year"))
	
		
	if not (user_month and user_day and user_year):

		self.response.out.write(user_year)
		self.response.out.write(user_day)
		self.response.out.write(user_month)
	
	else:
		self.response.out.write("Information ok!!!!!")

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
