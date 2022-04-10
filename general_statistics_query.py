GENERAL_STATISTICS_QUERY = """
with bool_table as (
    select count(*), likes.is_liked, likes.user_vk_id 
        from likes group by user_vk_id, is_liked order by user_vk_id)

select true_table.count as true_count,
       false_table.count as false_count,
       true_table.user_vk_id,
       users.full_name as full_name
    from (select * from bool_table where is_liked = true) true_table 
    full join 
        (select * from bool_table where is_liked = false) false_table 
            on false_table.user_vk_id = true_table.user_vk_id
    full join users on users.vk_id = true_table.user_vk_id
            limit $page_size
            offset ($page - 1) * $page_size;
"""

TOP_NINE_MEMES = """
select 
        count(*) as likes_count,
        filepath,
        meme_id 
    from memes 
    inner join likes 
        on likes.meme_id = memes.id 
    where likes.is_liked = true 
    group by filepath, meme_id 
    order by likes_count desc;"""

GRADES_OF_MEMES = """
with graded as (
    select count(*), likes.meme_id, is_liked 
        from likes 
        group by likes.meme_id, likes.is_liked),
grouped_grades as(
    select 
        coalesce(disliked.meme_id, likd.meme_id) as meme_id,
        coalesce(disliked.count, 0) as dislikes,
        coalesce(disliked.is_liked, likd.is_liked) as dis_grade,
        coalesce(likd.count, 0) as likes, coalesce(likd.is_liked,
        disliked.is_liked) as likd_grade 
        from 
            (select * from graded where graded.is_liked = false) disliked
        full join (select * from graded where graded.is_liked = true) likd 
        on disliked.meme_id = likd.meme_id)
select * from grouped_grades where grouped_grades.meme_id = $meme_db_id;"""
