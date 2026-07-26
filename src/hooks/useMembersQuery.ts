import { useQuery } from '@tanstack/react-query';import axios from 'axios';import { useMemberStore } from '@/store/memberStore';
export const useMembersQuery=()=>{const members=useMemberStore(s=>s.members);return useQuery({queryKey:['members',members.length,members.map(m=>m.updatedAt).join(',')],queryFn:async()=>{await axios.get('/').catch(()=>null);return members},staleTime:1000*60});};
