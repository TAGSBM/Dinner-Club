from openerp import models, fields
from openerp import api

class dinner_club(models.Model):

    _inherit = "res.partner"

    LastName = fields.Char('Last Name', size=25)
    nick_name = fields.Char('Nick Name', size=25)
    FirstName = fields.Char('First Name', size=15)
    MaleFemale = fields.Selection((('M','Male'), ('F','Female')), 'Gender')
    Age = fields.Integer('Age')
    AgeRange1 = fields.Integer('Age Range 1')
    AgeRange2 = fields.Integer('Age Range 2')
    PhoneHome = fields.Char('Home Phone', size=15)
    PhoneWork = fields.Char('Work Phone', size=15)
    PhoneMobile = fields.Char('Mobile Phone', size=15)
    Account = fields.Float('Account')
    MembershipFees = fields.Integer('Membership Fees')
    Suburb = fields.Char('Suburb', size=50)
    Rating = fields.Integer('Rating')
    LastDinnerDate = fields.Datetime('Last Dinner Date')
    LDD = fields.Datetime('Last Dinner Date')
    ExpiryDate = fields.Datetime('Expiry Date')
    Smoker = fields.Boolean('Smoker')
    Comments = fields.Text('Comments')
    Live = fields.Selection((('0','Not Live'), ('1','Active'), ('H','On Hold(NA)'), ('P','Partnered(NA)'), ('N','DO NOT CONTACT')), 'Live')
    PersonalReferral = fields.Boolean('Personal Referral')
    InterviewDate = fields.Datetime('Interview Date')
    Consultant = fields.Char('Interview Consultant', size=50)
    DedConsultant = fields.Char('Dedicated Consultant', size=50)
    PrefCoach = fields.Char('Preferred Coach', size=50)
    GoldDinnersRemaining = fields.Integer('Gold Dinners Remaining')
    PlatinumDinnersRemaining = fields.Integer('Platinum Dinners Remaining')
    LocationID = fields.Integer('LocationID')
    DinnerForTwoDinnersEntree = fields.Integer('Dinner For Two Dinners Entree')
    DinnerForTwoDinnersRegular = fields.Integer('Dinner For Two Dinners Regular')
    ClubDinnersRemaining = fields.Integer('Club Dinners Remaining')
    DinnerForTwoDinnersRemaining = fields.Integer('Dinner For Two Dinners Remaining')
    CouchingMinutes = fields.Integer('Couching Minutes')
    Title = fields.Char('Title', size=5)
    DOB = fields.Datetime('Date of Birth')
    StarSign = fields.Char('StarSign', size=10)
    MaritalStatus = fields.Selection((('D','Divorced'), ('S','Seperated'), ('W','Widowed'), ('N','Never Married'), ('M','Married'), ('C','Cohabbiting')), 'Marital Status')
    MaritalsYrs = fields.Char('Maritals Years', size=5)
    AloneSince = fields.Char('Alone Since', size=10)
    NoChildren = fields.Integer('No Children')
    Ages = fields.Char('Ages', size=12)
    NoHome = fields.Integer('No Home')
    OthersChildren = fields.Char('Other Children', size=50)
    Nationality = fields.Char('Origin', size=15)
    Citizenship = fields.Char('Permanent Residence', size=15)
    MotherNationality = fields.Char('Mother Nationality', size=15)
    FatherNationality = fields.Char('Father Nationality', size=15)
    MFYearsinOZ = fields.Integer('MF Years in Austrlaia')
    YourYearsinOZ = fields.Integer('Your Years in Country')
    Heightcm = fields.Integer('Height (cm)')
    Weightkg = fields.Integer('Weight (kg)')
    Drink = fields.Selection((('N','No'), ('S','Social'), ('Y','Yes'), ('O','Occasionally')), 'Drink')
    Religion = fields.Char('Religion', size=20)
    ReligionImpt = fields.Boolean('Religion Important')
    HairColour = fields.Char('Hair Colour', size=10)
    HairLength = fields.Char('Hair Length', size=10)
    EyeColour = fields.Char('Eye Colour', size=10)
    Politics = fields.Char('Politics', size=1)
    Home = fields.Selection((('R','Renting'), ('O','Owner'), ('B','Buying')),'Home Ownership')
    FurtherEducation = fields.Char('Education', size=50)
    Employer = fields.Char('Employer', size=25)
    Industry = fields.Char('Industry', size=35)
    Position = fields.Char('Position', size=30)
    JobDescription = fields.Char('Job Description', size=50)
    Ambition = fields.Char('Self Description', size=100)
    JoinReasons = fields.Char('Join Reasons', size=100)
    PreferredAgeMin = fields.Integer('Preferred Age Min')
    PreferredAgeMax = fields.Integer('Preferred Age Max')
    FoodThai = fields.Char('FoodThai', size=1)
    FoodVegetarian = fields.Char('FoodVegetarian', size=1)
    FoodInternational = fields.Char('FoodInternational', size=1)
    FoodGreek = fields.Char('FoodGreek', size=1)
    FoodFrench = fields.Char('FoodFrench', size=1)
    FoodItalian = fields.Char('FoodItalian', size=1)
    FoodIndian = fields.Char('FoodIndian', size=1)
    FoodAsian = fields.Char('FoodAsian', size=1)
    Heightft = fields.Char('Height (ft)', size=12)
    Weightst = fields.Char('Weight (st)', size=12)
    Interests = fields.Char('Interests', size=250)
    Education = fields.Char('Education', size=1)
    Description = fields.Char('Self Description', size=255)
    PreferredDinnerDays = fields.Char('Preferred Dinner Days', size=200)
    Build = fields.Selection((('slim','Slim'), ('average','Average'), ('solid','Solid')), 'Build')
    RelationshipStatus = fields.Selection((('s','Single'), ('dm','Dating Member'), ('d','Found Someone'), ('m','Matched(6+ Months)')), 'Relationship Status') 
    CareerHistory = fields.Text('Career History')
    RelationshipHistory = fields.Text('Relationship History')
    PreferredCandidates = fields.Text('Preferred Candidates')
    PrecludeCandidates = fields.Text('Preclude Candidates')
    PotentialCandidates = fields.Text('Potential Candidates')
    ConsultantNotes = fields.Text('Consultant Notes')
    DatesAvailable = fields.Text('Dates Available')
    DatesSelected = fields.Text('Dates Selected')
    WorkInProgress = fields.Text('Work In Progress')
    GrowUpCountry = fields.Text('Grow Up Country')
    ParentsLocation = fields.Text('Parents Location')
    SchoolPlace = fields.Text('School Place')
    HaveSiblings = fields.Text('Have Siblings')
    CandidateChildren = fields.Text('Candidate Children')
    LevelofEducation = fields.Text('Level of Education')
    CareerBackground = fields.Text('Career Background')
    CandidateEducation = fields.Text('Candidate Education')
    LineOfWork = fields.Text('Line Of Work')
    DescribeYourself = fields.Text('Describe Yourself')
    MeasureSuccess = fields.Text('Measure Success')
    MajorInterests = fields.Text('Major Interests')
    PassionateAbout = fields.Text('Passionate About')
    HavePets = fields.Text('Have Pets')
    PhysicalAttributes = fields.Text('Physical Attributes')
    KindPersonality = fields.Text('Kind Personality')
    StructureDinners = fields.Text('Structure Dinners')
    interest_sport_tennis = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Tennis')
    interest_sport_water_skiing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Water Skiing')
    interest_sport_cricket = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Cricket')
    interest_sport_gym = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Gym')
    interest_sport_running = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Running / Jogging')
    interest_sport_surfing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Surfing')
    interest_sport_aerobics = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Aerobics')
    interest_sport_cycling = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Cycling')
    interest_sport_walking = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Walking')
    interest_sport_exercise_classes = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Exercise Classes')
    interest_sport_golf = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Golf')
    interest_sport_squash = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Squash')
    interest_sport_football = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Footaball')
    interest_sport_snow_skiing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Snow Skiing')
    interest_sport_horse_riding = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Horse Riding')
    interest_sport_bush_walking = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Bush Walking')
    interest_sport_swimming = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Swimming')
    interest_sport_boating = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Boating')
    interest_sport_fishing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Fishing')
    interest_sport_yoga = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Yoga')
    interest_sport_camping = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Camping')
    interest_sport_other = fields.Char('Other Sports Interests', size=50)
    interest_leisure_literature = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Literature')
    interest_leisure_economics = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Economics')
    interest_leisure_politics = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Politics (interest)')
    interest_leisure_personal_development = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Personal Development')
    interest_leisure_astrology = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Astrology')
    interest_leisure_history = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'History')
    interest_leisure_current_affairs = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Current Affairs')
    interest_leisure_philosophy = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Philosophy')
    interest_leisure_psychology = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Psychology')
    interest_leisure_drama = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Drama')
    interest_leisure_other = fields.Char(' Other Leisure Interests')
    interest_art_films = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Films / Movies')
    interest_art_concerts = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Concerts')
    interest_art_ballet = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Ballet')
    interest_art_ballroom_dancing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Ballroom Dancing')
    interest_art_latin_dancing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Latin Dancing')
    interest_art_theatre = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Theatre')
    interest_art_opera = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Opera(Art)')
    interest_art_modern_dance = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Modern Dance')
    interest_art_art_galleries = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Art Galleries')
    interest_art_american_dancing = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'American Dancing')
    interest_art_other = fields.Char('Other Art Interests', size=50)
    interest_music_classical = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Classical')
    interest_music_opera = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Opera(Music)')
    interest_music_folk = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Folk')
    interest_music_jazz = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Jazz')
    interest_music_country = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Country')
    interest_music_light_classical = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Light Classical')
    interest_music_rb = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'R&B')
    interest_music_rock = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Rock')
    interest_music_pop = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Pop')
    interest_music_other = fields.Char('Music Other', size=50)
    interest_hobbies_travel = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Travel')
    interest_hobbies_gardening = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Gardening')
    interest_hobbies_musical_instruments = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Musical Instruments')
    interest_hobbies_other = fields.Char('Activities / Hobbies Other', size=50)
    block_list = fields.One2many('dinnerclub.blocked_members', 'member_block_id', 'Blocked Members')
    restaurant_block_list = fields.One2many('dinnerclub.blocked_restaurants', 'restaurant_block_id', 'Blocked Restaurants')
    primary_office_id = fields.Many2one('dinners.office','Primary Office')
    office_ids = fields.One2many('dinners.office','partner_ids','Offices')
    member_child_list = fields.One2many('dinnerclub.children', 'member_child_id', 'Member Child List')
    heightgeneric = fields.Char('Height')
    heightunit = fields.Selection((('cm','cm'), ('f','Feet / Inchs')), 'Height Unit')
    weightgeneric = fields.Integer('Weight')
    weightunit = fields.Selection((('kg','kg'), ('s','Stone / Pounds')), 'Weight Unit')
    days_ids = fields.Many2many('dinners.days', 'dinner_days', 'partner_id', 'dinner_day_id', 'Days')
    member_hold = fields.One2many('dinnerclub.hold_members', 'member_hold_id', 'Member Holds')
    contact_exchange = fields.One2many('dinnerclub.contact_exchange', 'member_exchange_id', 'Member Exchanges')
    interest_hobbies_renovating = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Renovating')
    interest_hobbies_cooking = fields.Selection((('i','Passive Interest'), ('a','Active Interest')), 'Cooking')
    attachments = fields.Many2many('ir.attachment', string="Attachments")
    interest_passive_string = fields.Char(compute='_passive_interest', store=True, string="Passive Interests")
    interest_active_string = fields.Char(compute='_active_interests', store=True, string="Active Interests")
    dinner_history = fields.One2many('event.registration', 'partner_id')

    @api.depends('interest_sport_tennis', 'interest_sport_water_skiing', 'interest_sport_cricket', 'interest_sport_gym', 'interest_sport_running', 'interest_sport_surfing', 'interest_sport_aerobics', 'interest_sport_cycling', 'interest_sport_walking', 'interest_sport_exercise_classes', 'interest_sport_golf', 'interest_sport_squash', 'interest_sport_football', 'interest_sport_snow_skiing', 'interest_sport_horse_riding', 'interest_sport_bush_walking', 'interest_sport_swimming', 'interest_sport_boating', 'interest_sport_fishing', 'interest_sport_yoga', 'interest_sport_camping', 'interest_leisure_literature', 'interest_leisure_economics', 'interest_leisure_politics', 'interest_leisure_personal_development', 'interest_leisure_astrology', 'interest_leisure_history', 'interest_leisure_current_affairs', 'interest_leisure_philosophy', 'interest_leisure_psychology', 'interest_leisure_drama', 'interest_art_films', 'interest_art_concerts', 'interest_art_ballet', 'interest_art_ballroom_dancing', 'interest_art_latin_dancing', 'interest_art_theatre', 'interest_art_opera', 'interest_art_modern_dance', 'interest_art_art_galleries', 'interest_art_american_dancing', 'interest_music_classical', 'interest_music_opera', 'interest_music_opera', 'interest_music_folk', 'interest_music_jazz', 'interest_music_country', 'interest_music_light_classical', 'interest_music_rb', 'interest_music_rock', 'interest_music_pop', 'interest_hobbies_travel', 'interest_hobbies_gardening', 'interest_hobbies_musical_instruments', 'interest_hobbies_cooking', 'interest_hobbies_renovating')
    def _passive_interest(self):
        interest_string = ""
        for record in self:
            if record.interest_sport_tennis == "i":
	        interest_string += "Tennis, "
    
            if record.interest_sport_water_skiing == "i":
	        interest_string += "Water Skiing, "      
    
            if record.interest_sport_cricket == "i":
	        interest_string += "Cricket, " 
    
            if record.interest_sport_gym == "i":
	        interest_string += "Gym, "            
    
            if record.interest_sport_running == "i":
	        interest_string += "Running, "            
    
            if record.interest_sport_surfing == "i":
	        interest_string += "Surfing, "            
    
            if record.interest_sport_aerobics == "i":
	        interest_string += "Aerobics, "            
    
            if record.interest_sport_cycling == "i":
	        interest_string += "Cycling, "            
    
            if record.interest_sport_walking == "i":
	        interest_string += "Walking, "            
    
            if record.interest_sport_exercise_classes == "i":
	        interest_string += "Exercise Classes, "            
    
            if record.interest_sport_golf == "i":
	        interest_string += "Golf, "            
    
            if record.interest_sport_squash == "i":
	        interest_string += "Squash, "            
    
            if record.interest_sport_football == "i":
	        interest_string += "Football, "            
    
            if record.interest_sport_snow_skiing == "i":
	        interest_string += "Snow Skiing, "            
    
            if record.interest_sport_horse_riding == "i":
	        interest_string += "Horse Riding, "            
    
            if record.interest_sport_bush_walking == "i":
	        interest_string += "Bush Walking, "            
    
            if record.interest_sport_swimming == "i":
	        interest_string += "Swimming, "            
    
            if record.interest_sport_boating == "i":
	        interest_string += "Boating, "            
    
            if record.interest_sport_fishing == "i":
	        interest_string += "Fishing, "            
    
            if record.interest_sport_yoga == "i":
	        interest_string += "Yoga, "            
    
            if record.interest_sport_camping == "i":
	        interest_string += "Camping, "            
    
            if record.interest_leisure_literature == "i":
	        interest_string += "Literature, "            
    
            if record.interest_leisure_economics == "i":
	        interest_string += "Economics, "            
    
            if record.interest_leisure_politics == "i":
	        interest_string += "Politics, "            
    
            if record.interest_leisure_personal_development == "i":
	        interest_string += "Personal Development, "            
    
            if record.interest_leisure_astrology == "i":
	        interest_string += "Astrology, "            
    
            if record.interest_leisure_history == "i":
	        interest_string += "History, "            
    
            if record.interest_leisure_current_affairs == "i":
	        interest_string += "Current Affairs, "            
    
            if record.interest_leisure_philosophy == "i":
	        interest_string += "Philosophy, "            
    
            if record.interest_leisure_psychology == "i":
	        interest_string += "Psychology, "            
    
            if record.interest_leisure_drama == "i":
	        interest_string += "Drama, "            
    
            if record.interest_art_films == "i":
	        interest_string += "Films, "            
    
            if record.interest_art_concerts == "i":
	        interest_string += "Concerts, "            
    
            if record.interest_art_ballet == "i":
	        interest_string += "Ballet, "            
    
            if record.interest_art_ballroom_dancing == "i":
	        interest_string += "Ballroom Dancing, "            
    
            if record.interest_art_latin_dancing == "i":
	        interest_string += "Latin Dancing, "            
    
            if record.interest_art_theatre == "i":
	        interest_string += "Art Theatre, "            
    
            if record.interest_art_opera == "i":
	        interest_string += "Opera Play, "            
    
            if record.interest_art_modern_dance == "i":
	        interest_string += "Modern Dance, "            
    
            if record.interest_art_art_galleries == "i":
	        interest_string += "Art Galleries, "            
    
            if record.interest_art_american_dancing == "i":
	        interest_string += "American Dancing, "            
    
            if record.interest_music_classical == "i":
	        interest_string += "Classical Music, "            
    
            if record.interest_music_opera == "i":
	        interest_string += "Opera Music, "            
    
            if record.interest_music_opera == "i":
	        interest_string += "Opera Music, "            
    
            if record.interest_music_folk == "i":
	        interest_string += "Folk Music, "            
    
            if record.interest_music_jazz == "i":
	        interest_string += "Jazz Music, "            
    
            if record.interest_music_country == "i":
	        interest_string += "Country Music, "            
    
            if record.interest_music_light_classical == "i":
	        interest_string += "Light Classical Music, "            
    
            if record.interest_music_rb == "i":
	        interest_string += "R&B Music, "            
    
            if record.interest_music_rock == "i":
	        interest_string += "Rock Music, "            
    
            if record.interest_music_pop == "i":
	        interest_string += "Pop Music, "            
    
            if record.interest_hobbies_travel == "i":
	        interest_string += "Travel, "            
            
            if record.interest_hobbies_gardening == "i":
	        interest_string += "Gardening, "            
            
            if record.interest_hobbies_musical_instruments == "i":
	        interest_string += "Musical Instruments, "
            
            if record.interest_hobbies_cooking == "i":
                interest_string += "Cooking, "
            
            if record.interest_hobbies_renovating == "i":
	        interest_string += "Renovating, "
	        
	    record.interest_passive_string = interest_string

    @api.depends('interest_sport_tennis', 'interest_sport_water_skiing', 'interest_sport_cricket', 'interest_sport_gym', 'interest_sport_running', 'interest_sport_surfing', 'interest_sport_aerobics', 'interest_sport_cycling', 'interest_sport_walking', 'interest_sport_exercise_classes', 'interest_sport_golf', 'interest_sport_squash', 'interest_sport_football', 'interest_sport_snow_skiing', 'interest_sport_horse_riding', 'interest_sport_bush_walking', 'interest_sport_swimming', 'interest_sport_boating', 'interest_sport_fishing', 'interest_sport_yoga', 'interest_sport_camping', 'interest_leisure_literature', 'interest_leisure_economics', 'interest_leisure_politics', 'interest_leisure_personal_development', 'interest_leisure_astrology', 'interest_leisure_history', 'interest_leisure_current_affairs', 'interest_leisure_philosophy', 'interest_leisure_psychology', 'interest_leisure_drama', 'interest_art_films', 'interest_art_concerts', 'interest_art_ballet', 'interest_art_ballroom_dancing', 'interest_art_latin_dancing', 'interest_art_theatre', 'interest_art_opera', 'interest_art_modern_dance', 'interest_art_art_galleries', 'interest_art_american_dancing', 'interest_music_classical', 'interest_music_opera', 'interest_music_opera', 'interest_music_folk', 'interest_music_jazz', 'interest_music_country', 'interest_music_light_classical', 'interest_music_rb', 'interest_music_rock', 'interest_music_pop', 'interest_hobbies_travel', 'interest_hobbies_gardening', 'interest_hobbies_musical_instruments', 'interest_hobbies_cooking', 'interest_hobbies_renovating')
    def _active_interests(self):
        active_interest_string = ""
        for record in self:
            if record.interest_sport_tennis == "a":
	        active_interest_string += "Tennis, "            
    
            if record.interest_sport_water_skiing == "a":
	        active_interest_string += "Water Skiing, "            
    
            if record.interest_sport_cricket == "a":
	        active_interest_string += "Cricket, "            
    
            if record.interest_sport_gym == "a":
	        active_interest_string += "Gym, "            
    
            if record.interest_sport_running == "a":
	        active_interest_string += "Running, "            
    
            if record.interest_sport_surfing == "a":
	        active_interest_string += "Surfing, "            
    
            if record.interest_sport_aerobics == "a":
	        active_interest_string += "Aerobics, "            
    
            if record.interest_sport_cycling == "a":
	        active_interest_string += "Cycling, "            
    
            if record.interest_sport_walking == "a":
	        active_interest_string += "Walking, "            
    
            if record.interest_sport_exercise_classes == "a":
	        active_interest_string += "Exercise Classes, "            
    
            if record.interest_sport_golf == "a":
	        active_interest_string += "Golf, "            
    
            if record.interest_sport_squash == "a":
	        active_interest_string += "Squash, "            
    
            if record.interest_sport_football == "a":
	        active_interest_string += "Football, "            
    
            if record.interest_sport_snow_skiing == "a":
	        active_interest_string += "Snow Skiing, "            
    
            if record.interest_sport_horse_riding == "a":
	        active_interest_string += "Horse Riding, "            
    
            if record.interest_sport_bush_walking == "a":
	        active_interest_string += "Bush Walking, "            
    
            if record.interest_sport_swimming == "a":
	        active_interest_string += "Swimming, "            
    
            if record.interest_sport_boating == "a":
	        active_interest_string += "Boating, "            
    
            if record.interest_sport_fishing == "a":
	        active_interest_string += "Fishing, "            
    
            if record.interest_sport_yoga == "a":
	        active_interest_string += "Yoga, "            
    
            if record.interest_sport_camping == "a":
	        active_interest_string += "Camping, "            
    
            if record.interest_leisure_literature == "a":
	        active_interest_string += "Literature, "            
    
            if record.interest_leisure_economics == "a":
	        active_interest_string += "Economics, "            
    
            if record.interest_leisure_politics == "a":
	        active_interest_string += "Politics, "            
    
            if record.interest_leisure_personal_development == "a":
	        active_interest_string += "Personal Development, "            
    
            if record.interest_leisure_astrology == "a":
	        active_interest_string += "Astrology, "            
    
            if record.interest_leisure_history == "a":
	        active_interest_string += "History, "            
    
            if record.interest_leisure_current_affairs == "a":
	        active_interest_string += "Current Affairs, "            
    
            if record.interest_leisure_philosophy == "a":
	        active_interest_string += "Philosophy, "            
    
            if record.interest_leisure_psychology == "a":
	        active_interest_string += "Psychology, "            
    
            if record.interest_leisure_drama == "a":
	        active_interest_string += "Drama, "            
    
            if record.interest_art_films == "a":
	        active_interest_string += "Films, "            
    
            if record.interest_art_concerts == "a":
	        active_interest_string += "Concerts, "            
    
            if record.interest_art_ballet == "a":
	        active_interest_string += "Ballet, "            
    
            if record.interest_art_ballroom_dancing == "a":
	        active_interest_string += "Ballroom Dancing, "            
    
            if record.interest_art_latin_dancing == "a":
	        active_interest_string += "Latin Dancing, "            
    
            if record.interest_art_theatre == "a":
	        active_interest_string += "Art Theatre, "            
    
            if record.interest_art_opera == "a":
	        active_interest_string += "Opera Play, "            
    
            if record.interest_art_modern_dance == "a":
	        active_interest_string += "Modern Dance, "            
    
            if record.interest_art_art_galleries == "a":
	        active_interest_string += "Art Galleries, "            
    
            if record.interest_art_american_dancing == "a":
	        active_interest_string += "American Dancing, "            
    
            if record.interest_music_classical == "a":
	        active_interest_string += "Classical Music, "            
    
            if record.interest_music_opera == "a":
	        active_interest_string += "Opera Music, "            
    
            if record.interest_music_opera == "a":
	        active_interest_string += "Opera Music, "            
    
            if record.interest_music_folk == "a":
	        active_interest_string += "Folk Music, "            
    
            if record.interest_music_jazz == "a":
	        active_interest_string += "Jazz Music, "            
    
            if record.interest_music_country == "a":
	        active_interest_string += "Country Music, "            
    
            if record.interest_music_light_classical == "a":
	        active_interest_string += "Light Classical Music, "            
    
            if record.interest_music_rb == "a":
	        active_interest_string += "R&B Music, "            
    
            if record.interest_music_rock == "a":
	        active_interest_string += "Rock Music, "            
    
            if record.interest_music_pop == "a":
	        active_interest_string += "Pop Music, "            
    
            if record.interest_hobbies_travel == "a":
	        active_interest_string += "Travel, "            
            
            if record.interest_hobbies_gardening == "a":
	        active_interest_string += "Gardening, "            
            
            if record.interest_hobbies_musical_instruments == "a":
	        active_interest_string += "Musical Instruments, "
            
            if record.interest_hobbies_cooking == "a":
                active_interest_string += "Cooking, "
            
            if record.interest_hobbies_renovating == "a":
	        active_interest_string += "Renovating, "
            
            record.interest_active_string = active_interest_string

class dinner_credit(models.Model):

    _inherit = "product.template"
    
    type = fields.Selection(selection_add=[('d','Dinner'),('c','Couching')]);

class dinner_days(models.Model):

    _name = "dinners.days"
    
    name = fields.Char('Day Name', size=50)
    
class blocked_members(models.Model):

    _name = "dinnerclub.blocked_members"
    
    member_block_id = fields.Many2one('res.partner','Block Member')
    member_block_reason = fields.Char('Block Reason')

class contact_exchanges(models.Model):

    _name = "dinnerclub.contact_exchange"
    
    member_exchange_id = fields.Many2one('res.partner','Contact Exchange')
    member_exchange_by = fields.Selection((('T','Themselves'),('A','Administration')),'Done By')
    member_exchange_with = fields.Many2one('res.partner','Exchange With')
    exchange_comment = fields.Text('Comments')
    exchange_time = fields.Datetime('Exchange Time')
    
class memmber_holds(models.Model):

    _name = "dinnerclub.hold_members"
    
    member_hold_id = fields.Many2one('res.partner','Member Hold')
    member_hold_start_time = fields.Datetime('Hold Start Time')
    member_hold_end_time = fields.Datetime('Hold Finish Time')
    member_hold_reason = fields.Text('Hold Reason')

class blocked_restaurants(models.Model):

    _name = "dinnerclub.blocked_restaurants"
    
    restaurant_block_id = fields.Many2one('dinners.restaurant','Block Restaurant')
    resaurant_block_reason = fields.Char('Block Reason')

class member_children(models.Model):

    _name = "dinnerclub.children"
    
    member_child_id = fields.Many2one('res.partner','Block Member')
    member_child_age = fields.Integer('Child Age')
    member_child_gender = fields.Selection((('M','Male'), ('F','Female')), 'Child Gender')