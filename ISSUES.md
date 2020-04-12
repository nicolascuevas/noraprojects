## Functionlaities
- Create order with Employee (Done)
- Asign a user_uuid SESSION to the employee that get in platform to keep their answers unique (Done)
- Fix menu enabled, only allow to choose meal before 11am in Santiago (Done)
- Fix the timezone in de created_At and Update_at in all models (Done)
- Date uniquenes un menu model (Done)
- Orders result base on menu (Done)
- Show orders count for nora (Done)
- Employees can edit their orders (Done)
- Use and asign SESSION to identify employees.
- employees can only make 1 order per meal
- prevent edit for old meals

## Celery

- dont send complex objects to celery tasks (options), user options array (Done)
- use dispatcher for signal (Ready)
- form validations for menu and dish creation (Done)
- create different task schedule after menus is created (Done)

## Tests

### Menu

#### model
- menu creation (Done)
- unique menu per date (Done)
- is activate before 11 (local time)

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
- show edit (Pending)
- validation showing (Pending)

###Order

#### Model
- create Order before 11 of the meal date (Done)
- create Order after 11 of the meal date (Dpne)
- edit order with employee id (Done)


#### views
- show new (Done)
- show edit (Done)
- show answer (Done)



