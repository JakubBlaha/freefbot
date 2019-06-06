from discord.ext.commands import Context
from discord import Embed


async def send_command_embed(ctx: Context,
                             content: str = '',
                             send=True,
                             show_invocation=True):
    '''
    Send an embed with an author and the content. Return embed.
    The returned embed will also be assigned to `ctx.output_embed`
    for future access.
    '''

    e = Embed(
        description=
        f'{content}{chr(10) * (not content.endswith("```"))}\n{f"`{ctx.message.content}`" * show_invocation * bool(ctx.message.content)}'
    )
    e.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    if send:
        await ctx.send(embed=e)
    if not ctx.message.pinned:
        await ctx.message.delete()

    ctx.output_embed = e
    return e