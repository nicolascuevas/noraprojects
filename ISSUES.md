## Functionlaities
- create order with Employee
- asign a user_uuid SESSION to the employee that get in platform to keep thei answers unique
- fix menu enabled, only allow to choose meal before 11am in Santiago
- 

## Celery

- dont send complex objects to celery tasks (options), user options array (Ready)
- use dispatcher for signal (Ready)
- form validations for menu and dish creation (Pending)
- create diferent task schedule after menus is created (Ready)

## Tests

### Menu

#### model
- menu creation (Pending)
- prevent menu creation with missing fields (Pending)
- unique menu per date (Pending)
- set task after create (Pending)

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

#### views
- show new (Pending)
- show edit (Pending)
- show answer (Pending)



