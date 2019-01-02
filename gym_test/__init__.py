import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='DanL-v0',
    entry_point='gym_test.envs:DanL',
)
