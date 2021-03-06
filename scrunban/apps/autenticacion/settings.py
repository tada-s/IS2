ADMIN_PROJECT_CREATION = ('admin_create_project', 'Creacion de proyectos')
ADMIN_ROLE_MANAGEMENT = ('admin_create_admin', 'Asignacion de roles administrativos')
ADMIN_USER_MANAGEMENT = ('admin_manage_user', 'Administracion de usuarios')
PROJECT_ROL_MANAGEMENT = ('project_rol_management', 'Administracion de roles de proyecto')
PROJECT_FLUJO_MANAGEMENT = ('project_flujo_management', 'Administracion de Flujos')
PROJECT_DEV_MANAGEMENT = ('project_dev_management', 'Administracion de Equipo de Desarrollo')
PROJECT_SPRINT_MANAGEMENT = ('project_sprint_management', 'Administracion de Sprints')
PROJECT_TUS_MANAGEMENET = ('project_tus_management', 'Administracion de Tipos de User Stories')
PROJECT_INFO_MANAGEMENT = ('project_info_management', 'Administracion del Proyecto')
PROJECT_US_MANAGEMENT = ('project_us_management', 'Administracion de User Stories')
PROJECT_US_DEVELOP = ('project_us_develop', 'Desarrollo de User Stories')
PROJECT_KANBAN_WATCH = ('project_kanban_watch', 'Visualizacion del Kanban')
PROJECT_PB_WATCH = ('project_pb_watch', 'Visualizacion del Product Backlog')
PROJECT_US_APROVE = ('project_us_aprove', 'Aprobar un User Story')


DEFAULT_PERMISSIONS = [
    ADMIN_PROJECT_CREATION,
    ADMIN_ROLE_MANAGEMENT,
    ADMIN_USER_MANAGEMENT,
    PROJECT_ROL_MANAGEMENT,
    PROJECT_FLUJO_MANAGEMENT,
    PROJECT_DEV_MANAGEMENT,
    PROJECT_SPRINT_MANAGEMENT,
    PROJECT_TUS_MANAGEMENET,
    PROJECT_INFO_MANAGEMENT,
    PROJECT_US_MANAGEMENT,
    PROJECT_US_DEVELOP,
    PROJECT_KANBAN_WATCH,
    PROJECT_PB_WATCH,
    PROJECT_US_APROVE
]

DEF_ROLE_ADMIN = ('system_admin', 'Administrador del Sistema',
                  [
                      ADMIN_PROJECT_CREATION,
                      ADMIN_ROLE_MANAGEMENT,
                      ADMIN_USER_MANAGEMENT
                  ])

DEF_ROLE_SCRUM_MASTER = ('scrum_master','Scrum Master',
                         [
                             PROJECT_ROL_MANAGEMENT,
                             PROJECT_FLUJO_MANAGEMENT,
                             PROJECT_DEV_MANAGEMENT,
                             PROJECT_SPRINT_MANAGEMENT,
                             PROJECT_TUS_MANAGEMENET,
                             PROJECT_INFO_MANAGEMENT,
                             PROJECT_US_MANAGEMENT,
                             PROJECT_US_DEVELOP,
                             PROJECT_KANBAN_WATCH,
                             PROJECT_PB_WATCH,
                             PROJECT_US_APROVE
                         ])

DEF_ROLE_DEV_TEAM = ('dev_team','Development Team',
                     [
                         PROJECT_US_DEVELOP,
                         PROJECT_KANBAN_WATCH,
                         PROJECT_PB_WATCH,
                     ])

DEF_ROLE_PRODUCT_OWNER = ('product_owner','Product Owner',
                          [
                              PROJECT_KANBAN_WATCH,
                              PROJECT_PB_WATCH,
                          ])


DEFAULT_ADMIN_ROLES = [
    DEF_ROLE_ADMIN
]

DEFAULT_PROJECT_ROLES = [
    DEF_ROLE_SCRUM_MASTER,
    DEF_ROLE_PRODUCT_OWNER,
    DEF_ROLE_DEV_TEAM
]
