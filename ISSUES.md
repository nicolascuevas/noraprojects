## Functionlaities
- create order with Employee (Done)
- asign a user_uuid SESSION to the employee that get in platform to keep their answers unique (Done)
- fix menu enabled, only allow to choose meal before 11am in Santiago (Pending)
- fix the timezone in de created_At and Update_at in all models (Done)
- date uniquenes un menu model
- orders result base on menu (pending)

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
- create option to menu (Pending)
- prevent create option without menu or description (Pending)
- edit option (Pending)

#### views
- show crea (Pending)
- show edit (Pending)
- validation showing (Pending)

###Order

#### Model
- create Order  (Pending)
- prevent prder creation withput al lvalues (Pending)
- edit order with employee id (Pending)
- create only before 11pm (localtime)


#### views
- show new (Pending)
- show edit (Pending)
- show answer (Pending)



