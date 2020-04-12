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
- Show form fields (Pending)
- Show model menu (Pending)
- show dished optons (Pending)
- show answers fto Nora (Pending)


###Option

#### Model
- create option to menu (Done)
- prevent create option without description (Done)

#### views
- show crea (Pending)
- show edit (Pending)
- validation showing (Pending)

###Order

#### Model
- create Order before 11 of the meal date (Pending)
- create Order after 11 of the meal date (Pending)
- edit order with employee id (Done)


#### views
- show new (Pending)
- show edit (Pending)
- show answer (Pending)



