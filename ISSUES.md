## Functionlaities
- Create order with Employee (Done)
- Asign a user_uuid SESSION to the employee that get in platform to keep their answers unique (Done)
- Fix menu enabled, only allow to choose meal before 11am in Santiago (Done)
- Fix the timezone in de created_At and Update_at in all models (Done)
- Date uniquenes un menu model (Done)
- Orders result base on menu (Done)
- Show orders count for nora (Done)
- Employees can edit their orders (Done)
- Use and asign SESSION to identify employees. (Done)
- employees can only make 1 order per meal(Done)
- prevent edit for old meals(Done)
- Forms does not have validation feedback to users(Done)
- documentation mistakes on importing users data (Done)
- fix Models in project (Done)
- Better time validation, all menus from today at 11 to the future could be updated by users base on Santiago's TZ (Done)
- rename folder myproject, bad practice for django project.(Done)
- create slack reminder at 9 (2 hours before menus due date ) of it's date when menu is created(Done)
- show orders summary to help Nora to prepare the lunch(Done)
- create test for models (Done)
- create test for views (Done)


## Celery

- dont send complex objects to celery tasks (options), user options array (Done)
- use dispatcher for signal (Done)
- form validations for menu and dish creation (Done)
- create different task schedule after menus is created (Done)

## Tests

### Menu

#### model
- menu creation (Done)
- unique menu per date (Done)
- is activate before 11 (local time) (done)

#### views
- Show new (Done)
- Show model menu (Done)
- show dished optons (Done)
- show answers fto Nora (Done)
- 


###Option

#### Model
- create option to menu (Done)
- prevent create option without description (Done)

#### views
- show create (Done)
- show edit (Done)
- validation showing (Done)

###Order

#### Model
- create Order before 11 of the meal date (Done)
- create Order after 11 of the meal date (Done)
- edit order with employee id (Done)


#### views
- show new (Done)
- show edit (Done)
- show answer (Done)



