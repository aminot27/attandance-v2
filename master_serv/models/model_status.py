"""
# Initial default status when register is created.
# Util for user account management
# The next status may be ACTIVE by any activation process.
"""
MODEL_STATUS_CREATED = 'CREATED'
MODEL_STATUS_UPDATED = 'UPDATED'

"""
# Is used for indicate if user account is active
"""
MODEL_STATUS_ACTIVE = 'ACTIVE'

"""
# Is used for indicate if user account or any register is inactive.
# Can be activate again
"""
MODEL_STATUS_INACTIVE = 'INACTIVE'

"""
# Is used for indicate if user account or any register is inactive and can not be changed again
"""
MODEL_STATUS_DELETED = 'DELETED'
