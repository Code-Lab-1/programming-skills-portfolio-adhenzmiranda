#exercise 4
def make_shirt(size='L', message='I love Python <3'):
  print("\nThis will be a", size, "-size T-shirt")
  print("And the desired message will be:\n", message, "\non your T-shirt! Enjoy!")

make_shirt()
make_shirt(size = 'M')
make_shirt('S', 'Programming sure takes a lot of time to learn!')
