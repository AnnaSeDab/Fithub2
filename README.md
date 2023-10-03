## Code Institute Milestone Project 4

# Fithub


## UI/UX

### Project goals

Fithub is a fictitious website combining e-commerce and fitness.
The goal is to create a brand that is recognisable in all aspects of fitness (merchandise, gyms and 'on demand' fitness plans).
On Fithub page users can but fitness related aparell and equipment as well as fitness plan they can follow. Website also contains a section dedicated to locating Fithub gyms.

### User Stories

As a User I would like to:

- Browse merchandise
- Buy merchandise
- Buy gym equipment
- Create a profile to allow me to check out quicker in the future
- Buy a frtness plan I can follow at home
- Follow fitness plan and mark my progress on the page
- Find a gym I could go to

### Page owner goals

As an owner of this page I would like to:

- be able to add new merchandise to the website
- be able to edit merchandise
- be able to delete merchandise
- be able to add new fitness plans to the website
- be able to edit fitness plans
- be able to delete fitness plans
- be able to add new gyms to the website
- be able to edit gyms
- be able to delete gyms

### Developer goals

Allow users to easily:

- register to the website
- log in to the website
- navigate through the site
- find items they want to buy
- be able to adjust quantity and sizes of the items
- check out safely
- find a fitness plan that suits them
- follow fitness plan by checking off each completed day
- find nearest gyms they could go to


## Design

### Wireframes

The wireframes for desktop view were developed first then mobile view and responsiveness was being checked while working on the project.

![Picture of wireframe for desktop devices](media/wireframes.png)

![Picture of wireframe for desktop devices](media/wireframes1.png)

![Picture of wireframe for desktop devices](media/wireframes2.png)


### Fonts

Font awesome was used to generate icons. They are present on many of the buttons.
Google fonts Josefin Sans was used as a basic font on the page and Edu QLD Beginner for the text over the hero image.

### Colour scheme

Main body of the page is kept in grey colours with few purple elements which harmonise withe the hero image. 
It creates a soft background to many product images which are not limited to any colur restroctions. 
Toasts and warnings have appropriate colours eg. text warning the card will be charged. 
Thanks to the gray base the page is not too visually overhelming. 


## Defensive design

Sites which should be available only for the superuser or legged in users are guarded by either or :

```
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
```
```
    @login_required
```

### Adresses Checked

results:
HP - Sent to home page
404
STL - Sent to log in page

| address | user not logged in | not superuser |
| --- | --- | --- |
| merchandise/add | STL | HP |
| gyms/add | STL | HP |
| plans/days | STL | HP |
| gyms/edit/1/ | STL | HP |
| gyms/delete/1/ | STL | HP |
| plans/edit/1/ | STL | HP |
| plans/editday/2/ | STL | HP |
| merchandise/edit/2/ | STL | HP |
| profile/management/add_plan | 404 | HP |
| profile/management/add_day | 404 | HP |
| profile/management/add_fitness_category | 404 | HP |
| plans/editctegory | 404 | HP |
| profile | STL | Yes as it should |
| merchandise | yes | yes |

Ideally user would not be sent to 404 so that needs to be fixed.
Also Merchandise contains all the merchandise including fitness plans which do ot show on merchandise page accesed form the menu, however there is no harm in access but could be fixed.

## Features

### Existing features

#### When not logged in

#### When logged in

### Information Architecture


## Technologies used


### Testing

| Action | User not logged in | User logged in | Superuser | Pass |
| --- | --- | --- | --- | --- |
|  Can register | Option available when clicking on the peron icon in the header nav. Email sent to the user and can be confirmed.  | Option not avaiable | Option not avaiable | Yes |
| Registering with email or username that has been already used | Account not created 'email/username already exists' information provided.  | Option not avaiable | Option not avaiable | Yes |
| Registering with noncompliant password | Adequate feedback provided 'This password is too short. It must contain at least 8 characters. This password is too common. This password is entirely numeric.' | Option not avaiable | Option not avaiable | Yes |
| Login | User needs to be registered to be able to log in | Option available when clicking on the peron icon in the header nav. | Option available when clicking on the peron icon in the header nav. | Yes but: Success message shows basked content. It could be fixed or left as it reminds the user that they have an unfinished shopping and might prompt them to check out. |
| Log out | Option not avaiable | Option available when clicking on the peron icon in the header nav. Sign out confirmation then requested. Sign out successful. | Option available when clicking on the peron icon in the header nav. Sign out confirmation then requested. Sign out successful. | Yes |
| Clicking on the Fithub logo | Takes user to the main page checked from fitness plans, merchandise and gym page. |  | <- The same checked also from profile and management page | Yes |
| Clicking shopping bag icon when it is empty | Shopping bag page with 'Your bag is empty.' message and keep shopping button which takes us to merchangise page |   | <- The same  | Yes |
| Clicking shopping bag icon when something is in it | Shoping bag page with all the contents as should be |   |  <- The same  |   |
|  |  |  |  |  |
| Fitness plans | Page shows fitness plans |   | <- The same |   |
| Clickin on a Fitness plan | Fitness plan page shows |   |  <- The same |   |
| Clicking Try Now button | Day plan page shows |   | <- The same |   |
| Clicking to open the youtube video | Opens the youtube video in a new tab |   | <- The same |   |
| Clicking workout complete | Takes us back to the day plan page |   | <- The same |   |
| Clicking add to bag when we don't have a plan yet | 'You have to be logged in to purchase a fitness plan' message shows | Adds fitness plan to the bag | <- The same |   |
| Clicking add to bag when we do have a plan | N/A | Not possible to add a plan | <- The same |  Yes |
| Clicking add to bag when we do have a plan in a bag already | N/A | Not possible to add a plan | <- The same |  Yes |
| Fitness plan in the bag | N/A | Only adjustment button showing is remove as we cannot have more than one fitness plan at the time | <- The same |  |
| Remove fitness plan from the bag | N/A | Fitness plan gets removed. We go tho the merchandise page | <- The same | BUG ideally we would got to the plans page |
|  |  |  |  |  |
| All Merchandise | We go to the merchandise page |   | <- The same |   |
| Workout equipment | We go to the merchandise page with Workout equipment showing |   | <- The same |   |
| Activeware | We go to the merchandise page with Activeware showing |   | <- The same |   |
| Click see all products | Merchandise page shows both workout equiplent and activeware |   |  <- The same |   |
| Click Activeware under a product price | Merchandise page shows activeware |   | <- The same |   |
| Click Workout equipment under a product price | Merchandise page shows workout equiplent |   | <- The same |   |
| Sort by various paramters |Products are mostly srted accordingly. No rating shows as the highest rating |   | <- The same | sorting BUG could be fixed easy to spot with few products but might be annoying with a lot of unrated products pushing to the front |
| Click on a product | Product page opens |   |  <- The same |   |
| Adjust quantity by buttons, arrows or input| Quantity adjusted |   |  <- The same |   |
| Attempt to go below 0 with buttons | Quantity does not go below zero |   |  <- The same |   |
| Attempt to go over 99 with buttons | Quantity does not go over unless adjusted by input |   | <- The same  |   |
| Add product with quantity over 99 by manual input | 'Please select value that is no more than 99' message appears and item not added to the bag |   | <- The same  |   |
| Add product with quantity below 0 by manual input | 'Please select value that is no less than 0' message appears and item not added to the bag |   | <- The same  |   |
| Click keep shopping on the item page| We go back to the merchandise page and nothing is added to the basket |   | <- The same |   |
| Item size showing and can be picked | Only for the items with sizes |   |  <- The same |   |
| Add item to the bag | Item added to the bag with correct size and quantity. Success toast is showing with picture and item description. Button to checkout showing |   | <- The same |   |
| Click checkout button from the toast | Going to the shopping bag. It is not check out yet but this way we can confirm on a full screenthat all is ok with our order |   | <- The same |   |
| Click product category on the bag page | We go back to the merchandise page with only relevant category showing |   | <- The same |   |
| In bag adjust item quantity by buttons, arrows or input| Quantity adjusted |   |   |   |
| In bag attempt to go below 0 | Quantity can go below if input manually. Item gets removed. Could be guarded but does not break the page | <- The same  |  <- The same | Could be better but does not break the page. Will be fixed in the future |
| In bag attempt to go over 99 | Quantity can go over if input manually | <- The same  |  <- The same | BUG, needs to be fixed |
| In bag remove item | Item removed |  <- The same |  <- The same | Yes  |
| Subtotal of items | Calculated acordingly and showing | <- The same | <- The same |  |
| Grand total | Calculated accordingly. Shows how much more for the delivery. | <- The same and fitness plan in the bag takes delivery to zero | <- The same | Yes |
| Secure checkout button on bag page | Takes us to the form | <- The same but the form is prefilled, information changed save in the profile if we choose to  | <- The Same |  |
| Adjust Bag on checkout page | Takes us back to the bag | <- The Same | <- The Same | Yes |
| On order page more shopping button | Takes us to the merchandise page | <- The Same | <- The Same | Yes |
| Create the account link on the check out page | Takes us to the log in page | N/A | N/A | Yes |
| Log in link on the check out page | Takes us to the log in page | N/A | N/A | Yes |
| Processing payment | Checks out, payment taken by stripe, webhook created | <- The same and order shows on my orders page | <- The same  | Yes |
|  |  |  |  |  |
| Gyms page | Shows all the gyms |   | <- The same |   |
| Clicking on the gym name | Gym page opens on a new tab |   | <- The same |   |
|  |  |  |  |  |
| My Profile | N/A | Accesible through person icon in the top right corner | <- The same | Yes |
| My info on profile page | N/A | info can be updated | <- The same | Yes |
| My Fitness plan | N/A | Showing our instance plan details if purchased, button to all fitness plans if not | <- The same | Yes |
| My orders | N/A | Shows past orders list | <- The same | Yes |
| Clicking on the order in my orders | N/A | Shows us order details with informtions adjusted so it is clear it is a past order | <- The same | Yes |
| Go back to the profile from past order page | N/A | takes us back to the profile | <- The same | Yes |
|  |  |  |  |  |
| Product management | Cannot access | Cannot access | Accesible from the navigation and profile for the superuser only | Yes |
| Links on the management page | N/A | N/A | Go to correct forms/ pages - checked one by one | Yes |
| Add Product form | N/A | N/A | Product cannot be added without required fields filled in but price can be zero minus. Product can be added with rating over 5.00 | Possible BUG with the pricing as it is a function accesed only by the store owner it is for them to decide if that functionality can be somehow used or it needs to be changed. BUG Rating field needs to be adjusted |
| Add Fitness plan | N/A | N/A | Cannot be added without required fields filled | Yes |
| Add Fitness day | N/A | N/A | Cannot be added without required fields filled | Yes |
| Add Fitness category | N/A | N/A | Cannot be added without required fields filled | Yes |
| Add Gym  | N/A | N/A | Cannot be added without required fields filled | Yes |
| Edit Product form | N/A | N/A | Same rules and BUGs as with adding a product | Same as adding the product |
| Cancel editing Product | N/A | N/A | Goes back to all product with product unchnged | Yes |
| Delete Product | N/A | N/A | Product deleted we go back to all products| Yes |
| Edit Fitness plan | N/A | N/A | Cannot be edited without required fields filled. When edited goes to the fitness plan details page | Yes |
| Cancel editing Fitness plan | N/A | N/A | Goes back to all fitness plans | Yes |
| Delete Fitness plan | N/A | N/A | Deleted and goes back to all fitness plans | Yes |
| Edit Fitness day | N/A | N/A | Cannot be edited without required fields filled | Yes |
| Cancel editing Fitness day | N/A | N/A | Goes back to all fitness days | Yes |
| Delete Fitness day | N/A | N/A | Deleted and goes back to all fitness days | Yes |
| Edit Fitness category | N/A | N/A | Can be acccesed from the all fitness plans page. Cannot be added without required fields filled | Yes |
| Cancel editing Fitness category | N/A | N/A | Can be acccesed from the all fitness plans page. Goes back to all fitness plans | Yes |
| Delete Fitness category | N/A | N/A | Can be acccesed from the all fitness plans page. Deleted and goes back to all fitness plans | Yes |
| Edit Gym  | N/A | N/A | Cannot be added without required fields filled | Yes |
| Cancel editing gym | N/A | N/A | Goes back to all gyms | Yes |
| Delete gym  | N/A | N/A | Deleted and goes back to gyms | Yes |
|  |  |  |  |  |
| Toasts showing | When items added, adjusted or removed toasts show as expected | <- The same  | <- The same  | Some of the items shoud get friendly name to show on toasts |

The mechanics of the fitness plan was tested by adjusting view to set earlier start-day. Current date, start_day, day_one.available_from, day_two.available_from, day_three.available_from were printed to the console to check if logic works. Fitness workout was available only on the days for which available_from date was equal or past today's date. Mechanics to check off each day as done after the workout needs to be added although user would have access to the previous workouts either. 
![Screenshot of the printed statements](media/screenshot.png)

### Manual testing


### Bugs

When performing CRUD operations toast would show contents of the bag. 
Toast type was chaneged to info and it's headline adjusted.


#### Unfixed bugs that are important to fix
The management - Management shoud have been put in a separate app.
Splitting it between different apps creates inconsistencies and makes the other apps less transparent.

Mechanics to check off each day as done after the workout needs to be added. It's lack, however, does not break the mechanics. 


## Credits

