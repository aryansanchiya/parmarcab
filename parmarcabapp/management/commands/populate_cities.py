from django.core.management.base import BaseCommand
from parmarcabapp.models import City

class Command(BaseCommand):
    help = 'Populate the database with city names in Gujarat, Rajasthan, and Maharashtra'

    def handle(self, *args, **kwargs):
        cities = {
            "Gujarat": [
                "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh",
                "Gandhinagar", "Anand", "Nadiad", "Morbi", "Bharuch", "Navsari", "Valsad", "Mehsana",
                "Bhuj", "Porbandar", "Surendranagar", "Patan", "Veraval", "Palanpur", "Vapi", "Botad",
                "Godhra", "Dahod", "Amreli", "Deesa", "Himmatnagar", "Idar", "Kalol", "Kapadvanj",
                "Dholka", "Dhrangadhra", "Mahesana", "Mansa", "Modasa", "Mundra", "Unjha", "Kadi",
                "Manavadar", "Mangrol", "Mandvi", "Matar", "Mithapur", "Morvi", "Paddhari", "Radhanpur",
                "Sidhpur", "Tharad", "Umreth", "Visnagar", "Vyara", "Wankaner"
            ],
            "Rajasthan": [
                "Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer", "Udaipur", "Bhilwara", "Alwar", "Bharatpur",
                "Pali", "Sikar", "Bhiwadi", "Sri Ganganagar", "Banswara", "Baran", "Barmer", "Bundi",
                "Chittorgarh", "Churu", "Dausa", "Dholpur", "Dungarpur", "Hanumangarh", "Jaisalmer",
                "Jhalawar", "Jhunjhunu", "Karauli", "Nagaur", "Pratapgarh", "Rajsamand", "Sawai Madhopur",
                "Sirohi", "Tonk", "Jhalrapatan", "Kishangarh", "Phalodi", "Sojat", "Makrana", "Sujangarh",
                "Nokha", "Deeg", "Nimbahera", "Beawar", "Bhinder", "Fatehpur", "Gajsinghpur", "Keshorai Patan",
                "Kumbhalgarh", "Rawatbhata"
            ],
            "Maharashtra": [
                "Mumbai", "Pune", "Nagpur", "Nashik", "Thane", "Aurangabad", "Solapur", "Amravati",
                "Kolhapur", "Akola", "Jalgaon", "Latur", "Dhule", "Ahmednagar", "Chandrapur", "Parbhani",
                "Sangli", "Nanded", "Malegaon", "Gondia", "Jalna", "Beed", "Wardha", "Yavatmal", "Satara",
                "Bhandara", "Ratnagiri", "Osmanabad", "Ambejogai", "Baramati", "Bhusawal", "Buldhana",
                "Chalisgaon", "Chiplun", "Dombivli", "Ichalkaranji", "Kalyan", "Karad", "Lonavala", "Mahad",
                "Malkapur", "Matheran", "Murtijapur", "Nagothana", "Nandurbar", "Pandharpur", "Pen",
                "Phaltan", "Rah"]
        }

        for state, city_names in cities.items():
            for name in city_names:
                City.objects.get_or_create(name=name, state=state)

        self.stdout.write(self.style.SUCCESS('Successfully populated city names'))