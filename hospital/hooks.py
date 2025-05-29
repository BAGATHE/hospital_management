import logging

_logger = logging.getLogger(__name__)

def assign_admin_hospital_group(env):
    admin_group = env.ref('base.group_system')
    hospital_admin_group = env.ref('hospital.group_hospital_admin')

    _logger.info("Début du post_init_hook assign_admin_hospital_group")

    for user in admin_group.users:
        if hospital_admin_group not in user.groups_id:
            user.groups_id = [(4, hospital_admin_group.id)]
            _logger.info(f"Ajout du groupe Admin Hospital à l'utilisateur {user.login}")
        else:
            _logger.info(f"L'utilisateur {user.login} a déjà le groupe Admin Hospital")

    _logger.info("Fin du post_init_hook assign_admin_hospital_group")
