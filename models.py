
class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='customer')
    address = models.CharField(max_length=255, blank=True)
    authority = models.CharField(max_length=255, blank=True)    # for manager
    pic = models.ImageField(upload_to='user', default='user/default.jpg')
    gender = models.CharField(max_length=255, blank=True, default='male')
    birthday = models.CharField(max_length=255, blank=True)
    preference = models.CharField(max_length=255, blank=True)




class Restaurant(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255, blank=True)
    introduction = models.TextField(blank=True)
    suburb = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=255, blank=True)
    cuisine = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    pic = models.ImageField(upload_to='restaurant', default='restaurant/default.png')


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0)
    pic = models.ImageField(upload_to='dish')
    restaurant = models.ForeignKey(Restaurant, related_name='menu')


class Concession(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    title = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=0)
    release_time = models.DateTimeField(auto_now_add=True)




