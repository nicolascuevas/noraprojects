## Functionalities
- Create order with Employee (Done)
- Asign a user_uuid SESSION to the employee that get in platform to keep their answers unique (Done)
- Fix menu enabled, only allow to choose meal before 11am in Santiago (Done)
- Fix the timezone in de created_At and Update_at in all models (Done)
- Date uniquenes un menu model (Done)
- Orders result base on menu (Done)
- Show orders count for nora (Done)
- Employees can edit their orders (Done)
- Use and asign SESSION to identify employees. (Done)
- Employees can only make 1 order per meal(Done)
- Prevent edit for old meals(Done)
- Forms does not have validation feedback to users(Done)
- Documentation mistakes on importing users data (Done)
- Fix Models in project (Done)
- Better time validation, all menus from today at 11 to the future could be updated by users base on Santiago's TZ (Done)
- Rename folder myproject, bad practice for django project.(Done)
- Create slack reminder at 9 (2 hours before menus due date ) of it's date when menu is created(Done)
- Show orders summary to help Nora to prepare the lunch(Done)
- Create test for models (Done)
- Create test for views (Done)


## Celery

- Dont send complex objects to celery tasks (options), user options array (Done)
- Use dispatcher for signal (Done)
- Form validations for menu and dish creation (Done)
- Create different task schedule after menus is created (Done)

## Tests

### Menu

#### model
- Menu creation (Done)
- Unique menu per date (Done)
- Is activate before 11 (local time) (done)

#### views
- Show new (Done)
- Show model menu (Done)
- Show dished optons (Done)
- Show answers fto Nora (Done)
- 


### Option

#### Model
- Create option to menu (Done)
- Prevent create option without description (Done)

#### views
- Show create (Done)
- Show edit (Done)
- Validation showing (Done)

### Order

#### Model
- Create Order before 11 of the meal date (Done)
- Create Order after 11 of the meal date (Done)
- Edit order with employee id (Done)


#### views
- Show new (Done)
- Show edit (Done)
- Show answer (Done)



